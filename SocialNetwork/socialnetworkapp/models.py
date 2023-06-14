from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/', null=True, default='images/default_profile.png')
    faculty = models.CharField(max_length=255)
    hobbies = models.CharField(null=True, max_length=255)
    major = models.CharField(max_length=255)

    def __str__(self):
        return str(self.uid)  
   
class Educator(models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.uid)

class Student(models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.uid)

class Chatroom(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE,related_name='created_chatrooms')
    recipient = models.TextField()
    created_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now=True)

class Chat(models.Model):
    chat_content = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now=True)
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now=True)
    reaction = models.ManyToManyField(User, related_name='posts')
    
    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    content = models.TextField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now=True)
    
    def __str__(self):
         return f"Comment by {self.uid} on Post {self.post}"

class Report(models.Model):
    content = models.TextField()
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now=True)
    
    def __str__(self):
        return str(self.uid)
