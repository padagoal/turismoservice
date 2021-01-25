from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.core import serializers


# Create your views here.

def index_blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/index_interno.html', {'posts': posts})


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

    return render(request, 'blog/login_blog.html')


def logout_user_blog(request):
    logout(request)
    return redirect(index_blog)


def register_blog(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        email = request.POST['email']
        User.objects.create_user(username=username,password=password,email=email)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Sin Acceso')
        else:
            login(request, user)
            return redirect(index_blog)

    return render(request,'blog/register_blog.html')


@login_required(login_url='blog/login/')
def likePost(request):
    post = request.POST.get('postliked')
    postliked = Post.objects.get(pk=post)

    likeByUserValidate = LikesPerUser.objects.filter(user=request.user.id,post_liked=postliked)

    if len(likeByUserValidate)>0:
        postliked.likes = postliked.likes - 1

        postliked.save()

        likeByUserValidate.delete()

        return JsonResponse(serializers.serialize('json', Post.objects.filter(pk=post)), safe=False, status=200)

    postliked.likes = postliked.likes+1

    postliked.save()

    formLikeByUser = LikePostForm()

    likeByUser = formLikeByUser.save(commit=False)
    likeByUser.post_liked = postliked
    likeByUser.user = request.user.id

    likeByUser.save()

    return JsonResponse(serializers.serialize('json',Post.objects.filter(pk=post)),safe=False,status=200)



