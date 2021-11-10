from django.urls import path
from .views import BlogDetailView

urlpatterns = [
    path('<int:pk>/', BlogDetailView.as_view(), name = 'blog_detail'),
]