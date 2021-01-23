from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.

def index_blog(request):
    return render(request, 'blog/index_interno.html', {})


def post_user(request):
    if request.user:
        posts = Post.objects.filter(author=request.user)
    else:
        return redirect(index_blog)

    return render(request, 'blog/index_user.html', {'posts': posts})


def post_new(request):
    if request.method == "POST":

        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_user)
        else:
            return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


def login_user_blog(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Sin Acceso')
        else:
            login(request, user)
            return redirect(index_blog)

    return render(request, 'Login_v5/index.html')


def logout_user_blog(request):
    logout(request)
    return redirect(index_blog)
