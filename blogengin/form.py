from django.forms import ModelForm
from blogengin.models import Post, Comment

class PostForm (ModelForm):
	class Meta:
		model = Post
		fields = ['cid', 'title', 'body', 'slug']