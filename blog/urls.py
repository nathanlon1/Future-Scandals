from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views
from .views import (
    BlogDetailView,
    BlogPostLike,
)
#from . import views


#


urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name = 'blog_detail'),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name='blogpost_like'),
]
