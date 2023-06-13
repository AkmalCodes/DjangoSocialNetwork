from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('', views.loginpage, name= 'login'),
    path('logout/', views.logoutuser, name= 'logout'),
    path('aboutus/', views.aboutus, name= 'aboutus'),
    
    #home & Posts
    path('home', views.home, name="home"),
    path('createPost/', views.createPost, name="createPost"),
    path('post/<int:pk>/delete/', views.delete_post_view, name='delete_post'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('createReport/<int:post_id>', views.submit_report, name='createReport'),
    
    #chats 
    path('chatroom/', views.chatroom, name="chatroom"),
    path('chatrooms/create/', views.chatroomform, name='create_chatroom'),
    path('chatrooms/chatroomform/', views.createChatroom, name='chatroomform'),
    path('chatrooms/', views.chatroomName, name='chatroomName'),
    path('chatroomchats/<int:chatroom_id>/', views.chatroom_chats, name='chatroomchats'),
    path('chatroom/<int:chatroom_id>/add_chat/', views.add_chat, name='add_chat'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('search-users/', views.search_users, name='search_users'),
    
    #profile
    path('userprofile/', views.userprofile, name="userprofile"),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('password/',views.PasswordsChangeView.as_view(template_name='socialnetworkapp/profilechangepassword.html'),name='password_change'),
    
    #reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
]
