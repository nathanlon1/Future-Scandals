from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post

class PostAdmin(MarkdownxModelAdmin):
    model = Post
    list_display = ['title','author','date_published','date_modified',]
    fieldsets = MarkdownxModelAdmin.fieldsets

admin.site.register(Post, PostAdmin)