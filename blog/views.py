# In views.py
from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'home.html', {'posts': posts})
