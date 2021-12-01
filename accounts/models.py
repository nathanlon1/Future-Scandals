from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    displayName = models.CharField(max_length=150)
    
    
    # Manually override save function
    # https://stackoverflow.com/questions/4380879/django-model-field-default-based-off-another-field-in-same-model
    # https://docs.djangoproject.com/en/3.2/topics/db/models/#overriding-model-methods (More accurate and clear)
    
    def save(self, *args, **kwargs):
        if not self.displayName:
            self.displayName = self.username
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ShowProfileView')
