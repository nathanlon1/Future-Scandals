from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
#
from django.conf import settings
#
from django.contrib.auth.models import User
#

from markdownx.models import MarkdownxField
#
User = settings.AUTH_USER_MODEL
#
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()
    
    date_published = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = "blogs",
    )

    likes = models.ManyToManyField(User, related_name='blogpost_like')



    
    def body_summary(self):
        return self.body[:300]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date_published',]

'''
class Profile(models.Model):
    user = models.OneToOneField(CustomUser,null=True on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
'''

        
class Comment(models.Model):
    post = models.ForeignKey(
    Post, 
    related_name="comments", 
    on_delete=models.CASCADE,
    )
    
    name = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    class Meta:
        ordering = ['-date_added',]
    
    

