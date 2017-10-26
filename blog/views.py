from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.order_by("id").reverse()
    return render(request, 'blog/posts.html', {'posts':posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')
