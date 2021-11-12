from django.shortcuts import render
from django.views.generic import ListView
from .models import Article
from blog.models import Post


class ArticleListView(ListView):
    model = Post
    template_name = 'home.html'
