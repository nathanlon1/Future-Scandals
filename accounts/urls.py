from django.urls import path
from .views import SignUpView, ShowProfileView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/', ShowProfileView.as_view(), name='show_profile_page'),

]
