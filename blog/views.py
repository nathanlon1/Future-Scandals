from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import Post

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    success_url = reverse_lazy('home')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user