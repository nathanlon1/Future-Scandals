from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Post, Comment
from .forms import CommentForm
#
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
#



class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'


    def get_context_data(self, **kwargs):
       
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data
    
#

def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))
#
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    #success_url = reverse_lazy('home')
    def form_valid(self, form):
       form.instance.post_id = self.kwargs['pk']
       return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk':self.kwargs['pk']})

