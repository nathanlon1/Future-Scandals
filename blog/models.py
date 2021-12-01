from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from markdownx.models import MarkdownxField

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()
    
    date_published = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    
    def body_summary(self):
        return self.body[:300]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-date_published',]
'''
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,null=True on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
'''

