from django.urls import path
from .views import BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name = 'blog_detail'),
    path('new/', BlogCreateView.as_view(), name = 'blog_create'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name = 'blog_edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name = 'blog_delete'),
]