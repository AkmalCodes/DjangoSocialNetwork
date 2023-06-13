from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash,authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from .models import *
from .forms import *

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists in the database
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return render(request, 'socialnetworkapp/signin.html')

        # Authenticate the user
        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is not None:
            # Login the authenticated user
            login(request, authenticated_user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'socialnetworkapp/signin.html')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile_edit') # redirect to profile_edit page

@login_required
def logoutuser(request):
    logout(request)
    return redirect('login')

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'socialnetworkapp/home.html',context)


@login_required
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Create an instance of the Post model without saving it to the database
            post.uid = request.user  # Set the uid field to the current user
            post.save()  # Save the post to the database
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'socialnetworkapp/postsCreate.html', context)

@login_required
def createChatroom(request):
    form = ChatroomForm()
    if request.method == 'POST':
        form = ChatroomForm(request.POST)
        if form.is_valid():
            recipient_username = form.cleaned_data['recipient']
            
            existing_chatrooms = Chatroom.objects.filter(
                uid=request.user,
                recipient=recipient_username
            )
            
            if existing_chatrooms.exists():
                form.add_error('recipient', 'You already have a chatroom with this recipient.')
            elif User.objects.filter(username=recipient_username).exists():
                chatroom = form.save(commit=False)
                chatroom.uid = request.user
                chatroom.save()
                return redirect('home')
            else:
                form.add_error('recipient', 'Invalid recipient username.')

    context = {'form': form}
    return render(request, 'socialnetworkapp/chatroomform.html', context)

@login_required
def chatroomName(request):
    username = request.user.username
    chatrooms = Chatroom.objects.filter(Q(uid__username=username) | Q(recipient=username)).select_related('uid')
    context = {'chatrooms': chatrooms}
    return render(request, 'socialnetworkapp/chatroom.html', context)

@login_required
def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.uid == request.user:
        if request.method == 'POST':
            post.delete()
            return redirect('home')  # Redirect to the desired page after deletion
        return render(request, 'delete_post.html', {'post': post})
    else:
        return redirect('home')  # Redirect to an appropriate page if the user is not the author

@login_required
def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.uid = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    comments = Comment.objects.filter(post=post)  # Fetch all comments related to the post

    return render(request, 'socialnetworkapp/postsview.html', {'post': post, 'comment_form': comment_form, 'comments': comments})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.reaction.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
    
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST' and request.user == comment.uid:
        comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def add_chat(request, chatroom_id):
    if request.method == 'POST':
        chat_content = request.POST['chat_content']
        chatroom = Chatroom.objects.get(id=chatroom_id)
        chat = Chat.objects.create(
            chat_content=chat_content,
            chatroom=chatroom,
            uid=request.user
        )
        #return redirect('chatroomchats', chatroom_id=chatroom_id)
        return HttpResponseRedirect(reverse('chatroomchats', args=[str(chatroom_id)]))

    return redirect('home')  # Redirect to home if it's not a POST request

@login_required
def chatroom_chats(request, chatroom_id):
    chatroom = get_object_or_404(Chatroom, id=chatroom_id)
    chats = Chat.objects.filter(chatroom=chatroom)
    
    context = {
        'chatroom': chatroom,
        'chats': chats,
    }    
    return render(request, 'socialnetworkapp/chatroomchats.html', context)

@login_required
def chatroom(request):
    return render (request, 'socialnetworkapp/chatroom.html')

@login_required
def chatroomform(request):
    return render (request, 'socialnetworkapp/chatroomform.html')

@login_required
def userprofile(request):
    return render (request, 'socialnetworkapp/profile.html')

def profile_edit(request):
    # Logic for handling the profile edit page
    # Retrieve the current user's profile and pass it to the template
    user_profile = request.user.userprofile
    context = {
        'user_profile': user_profile
    }
    return render(request, 'socialnetworkapp/profileEdit.html', context)

@login_required
def profile_edit(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.user = request.user
            profile_form.save()
            return redirect('profile_edit')
    else:
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'socialnetworkapp/profileEdit.html', context)


@login_required
def search_users(request):
    search_query = request.GET.get('search_query', '')
    users = User.objects.filter(username__icontains=search_query)
    user_list = [{'username': user.username} for user in users]
    return JsonResponse(user_list, safe=False)

@login_required
def submit_report(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    form = SubmitReport()
    if request.method == 'POST':
        form = SubmitReport(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.uid = request.user
            report.post = post  # Set the post field to the retrieved post
            report.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'socialnetworkapp/reportcreate.html', context)


def aboutus(request):
    return render (request, 'socialnetworkapp/aboutus.html')
