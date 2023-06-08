from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.loginpage, name= 'login'),
    path('logout/', views.logoutuser, name= 'logout'),
    path('home', views.home, name="home"),
    path('createPost/', views.createPost, name="createPost"),
    path('post/<int:pk>/delete/', views.delete_post_view, name='delete_post'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('chatroom/', views.chatroom, name="chatroom"),
    path('chatrooms/create/', views.chatroomform, name='create_chatroom'),
    path('chatrooms/chatroomform/', views.createChatroom, name='chatroomform'),
    path('chatrooms/', views.chatroomName, name='chatroomName'),
    path('chatroomchats/<int:chatroom_id>/', views.chatroom_chats, name='chatroomchats'),
    path('chatroom/<int:chatroom_id>/add_chat/', views.add_chat, name='add_chat'),
    path('userprofile/', views.userprofile, name="userprofile"),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    # path('profile/edit/password', auth_views.PasswordChangeView.as_view(template_name='socialnetworkapp/profilechangepassword.html')),
    path('password/',views.PasswordsChangeView.as_view(template_name='socialnetworkapp/profilechangepassword.html'),name='password_change'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('search-users/', views.search_users, name='search_users'),
]
