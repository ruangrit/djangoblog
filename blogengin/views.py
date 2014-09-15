from django.shortcuts import render, get_object_or_404
from blogengin.models import Post

# Create your views here.
def index(request):
	posts = Post.objects.order_by('-created')
	return render(request, 'blogengin/list.html', {'posts': posts})


