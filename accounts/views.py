from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ShowProfileView(DetailView):
    model = CustomUser
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = CustomUser.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

