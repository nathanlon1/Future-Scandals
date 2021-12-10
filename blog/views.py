from django.shortcuts import render

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.http import HttpResponseForbidden


from .models import Post, Comment
from .forms import CommentForm
#
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
#

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




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

        #
        comments_connected=Comment.objects.filter(
            post=self.get_object()).order_by('-date_added')
        data['comments']=comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
            #
        return data
        #
    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'),
                              name=self.request.user,
                              post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)
        #



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


def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))
#
#

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    fields = ['body']
    #success_url = reverse_lazy('home')
    def form_valid(self, form):
       form.instance.post_id = self.kwargs['pk']
       form.instance.name = self.request.user
       return super().form_valid(form)
   
    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk':self.kwargs['pk']})
    @login_required
    def add_comment(request, post_id):
        if request.method == 'POST':
            form=CommentForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
class OwnerProtectMixin(object):
    def dispatch(self, request, *args, **kwargs):
        objectUser = self.get_object()
        if objectUser.name != self.request.user:
            return HttpResponseForbidden()
        return super(OwnerProtectMixin, self).dispatch(request, *args, **kwargs)
   

#class CommentUpdateView(UpdateView):
    #model = Comment
    #fields = [ 'body',]
    #def test_func(self):
        #obj = self.get_object()
        #return obj.name == self.request.user
    
    #def handle_no_permission(self):
        #return redirect('users:create-profile')

@method_decorator(login_required, name='dispatch')
class CommentDeleteView(OwnerProtectMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('home')
    
       

    
   

