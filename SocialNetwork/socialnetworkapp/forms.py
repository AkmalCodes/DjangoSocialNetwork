from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        
class updateProfileFormEducator(ModelForm):
    class Meta:
        model = Educator
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
class SubmitReport(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['content']

class ChatroomForm(forms.ModelForm):
    class Meta:
        model = Chatroom
        fields = ['recipient']

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['chat_content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(label='profile picture')
   
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
        
class PasswordEditForm(PasswordChangeForm):
    pass



