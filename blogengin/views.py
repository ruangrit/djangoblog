from django.shortcuts import render, get_object_or_404
from blogengin.models import Post, Comment, Category
from django.http import HttpResponseRedirect
from blogengin.form import PostForm 
# Create your views here.
def list(request, cid):
	posts = Post.objects.filter(cid=cid).order_by('-created')
	return render(request, 'blogengin/list.html', {'posts': posts})

def index(request):
	cats = Category.objects.order_by('title')
	return render(request, 'blogengin/index.html', {'cats': cats})

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blogengin/post.html', {'post': post})

def post_form(request):
	if request.method == 'POST':
		
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()	
			
	return render(request, 'blogengin/post_add.html', {'form': PostForm})




