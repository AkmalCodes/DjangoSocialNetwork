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
    class Meta:
        model = UserProfile
        exclude = ['user']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control'}),
            'hobbies': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PasswordEditForm(PasswordChangeForm):
    pass

