from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from .models import Category, Comment, Post
from .forms import CommentForm, CommentResponseForm

def home(request):
    return render(request, 'post/home.html')

def posts(request):
    template = 'post/posts.html'
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, template, context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    related_posts = Post.objects.filter(Q(category=post.category))
    if request.method == 'GET':
        form = CommentForm()
        template = 'post/detail.html'
        context = {
            'form': form,
            'post': post,
            'related_posts': related_posts,
        }

        return render(request, template, context)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()

            return redirect(reverse('post:post_detail', args=(pk,)))

def commentReply(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'GET':
        form = CommentResponseForm()
        template = 'post/commentResponse.html'
        context = {
            'comment': comment,
            'form': form,
        }
        return render(request, template, context)
    if request.method == 'POST':
        form = CommentResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.comment = comment
            response.save()

            return redirect(reverse('post:comment_reply', args=(pk,)))

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    categories = Category.objects.filter(category__icontains=query)
    context = {
        'query': query,
        'posts': posts,
        'categories': categories,
    }    

    return render(request, 'post/search.html', context)

def category_posts(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'category': category,
    }
    return render(request, 'post/category_posts.html', context)
