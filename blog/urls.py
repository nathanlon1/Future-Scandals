from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views
from .views import (
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogPostLike,
    AddCommentView,
    #CommentUpdateView,
    CommentDeleteView,
)
#from . import views


#


urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name = 'blog_detail'),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name='blogpost_like'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('new/', BlogCreateView.as_view(), name = 'blog_create'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name = 'blog_edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name = 'blog_delete'),
    path('delete-comment/<int:pk>', CommentDeleteView.as_view(), name='delete-comment'),
    #path('edit-comment/<int:pk>', CommentUpdateView.as_view(), name = 'edit-comment'),
]
