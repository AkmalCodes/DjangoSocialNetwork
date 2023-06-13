from django.contrib import admin
from .models import UserProfile, Educator, Student, Chatroom, Chat, Post, Comment, Report

admin.site.register(UserProfile)
admin.site.register(Educator)
admin.site.register(Student)
admin.site.register(Chatroom)
admin.site.register(Chat)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Report)
