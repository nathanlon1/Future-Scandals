from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'