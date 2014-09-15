from django.shortcuts import render, get_object_or_404
from blogengin.models import Post
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-created')
	return render(request, 'blogengin/list.html', {'posts': posts})

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blogengin/post.html', {'post': post})

def post_form(request):
	posts = Post.objects.order_by('-created')
	return render(request, 'blogengin/list.html', {'posts': posts})


