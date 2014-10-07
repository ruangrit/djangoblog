from django.shortcuts import render, get_object_or_404, render_to_response
from blogengin.models import Post, Comment, Category
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from blogengin.form import PostForm ,MyRegistrationForm
from pprint import pprint

from django.contrib import auth                 
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf 
from django.template import RequestContext
# Create your views here.
def list(request, cid):
	posts = Post.objects.filter(cid=cid).order_by('-created')
	cat = Category.objects.get(cid=cid)
	my_record = Category.objects.get(cid=1)
	form = PostForm(instance=my_record)
	pprint(vars(form))
	return render(request, 'blogengin/list.html', {'posts': posts, 'cat': cat})

def index(request):
	cats = Category.objects.order_by('title')
	return render(request, 'blogengin/index.html', {'cats': cats})

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blogengin/post.html', {'post': post})

def post_form(request, slug=None):
	if slug:
		instance = get_object_or_404(Post, slug=slug)
		form = PostForm(request.POST or None, instance=instance)
	else:
		form = PostForm(request.POST)
	if form.is_valid():
		#pprint(vars(form))
		#print form.cleaned_data[body]
		new_post = form.save()

		return HttpResponseRedirect(reverse(list, args=(new_post.cid_id,)))
	return render(request, 'blogengin/post_add.html', {'form': form})
def post_delete(request, slug):
	if slug:
		Post.objects.filter(slug=slug).delete()
		return HttpResponseRedirect('/')
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/accounts/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print args
    return render(request, 'blogengin/register.html', args)


def user_login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('blogengin/login.html', context_instance=RequestContext(request))
