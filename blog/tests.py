from django.test import TestCase
from django.urls import reverse

from .models import Post
from django.contrib.auth import get_user_model

class PostTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "testacc",
            email = "test@email.com",
            password = "passwoooooojakldjaslkdjas",
        )
        self.post = Post.objects.create(
            title = "title",
            body = "body",
            author = self.user,
        )
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "title")
        self.assertEqual(f"{self.post.body}", "body")
        self.assertEqual(f"{self.post.author}", "testacc")
    
    def test_post_detail_View(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog_detail.html")

    