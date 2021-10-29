from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date = models.DateTimeField(auto_now_add=True)
    displayName = models.CharField(max_length=150)
    
    # Manually override save function
    # https://stackoverflow.com/questions/4380879/django-model-field-default-based-off-another-field-in-same-model
    
    def save(self, *args, **kwargs):
        if not self.displayName:
            self.displayName = self.username
        super().save(*args, **kwargs)