from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.order_by("id").reverse()
    return render(request, 'blog/posts.html', {'posts':posts})
