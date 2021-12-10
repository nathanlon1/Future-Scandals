from django.test import TestCase
from django.urls import reverse

class HomeTests(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('blog_list'))

    def test_new_posts_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
