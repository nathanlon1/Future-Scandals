from django.urls import path
from .views import(
    HomePageView,
    BlogListView,
    BlogListViewPopular
    )

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/', BlogListView.as_view(), name='blog_list'),
    path('new/', BlogListViewPopular.as_view(), name='popularblog_list'),

]
