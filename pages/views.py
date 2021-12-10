from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Post
from accounts.models import CustomUser 


from django.http import HttpResponseRedirect



class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get(self, request):
        return HttpResponseRedirect("new/")

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogListViewPopular(ListView):
    model = Post
    template_name = 'home.html'
    #queryset =Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')
    #context_object_name = 'popularblog_list'
