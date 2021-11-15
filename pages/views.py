from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Post


class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

