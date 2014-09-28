from django.forms import ModelForm
from blogengin.models import Post, Comment
from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm    

class PostForm (ModelForm):
	class Meta:
		model = Post
		fields = ['cid', 'title', 'body', 'slug']

class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

