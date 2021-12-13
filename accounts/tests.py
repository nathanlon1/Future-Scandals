from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

class PostTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "testacc",
            email = "test@email.com",
            password = "passwoooooojakldjaslkdjas",
        )
    
    def test_account_content(self):
        self.assertEqual(f"{self.user.username}", "testacc")
        self.assertEqual(f"{self.user.displayName}", "testacc")
        self.assertEqual(f"{self.user.email}", "test@email.com")
    
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
    
    def test_profile_view(self):
        response = self.client.get(reverse('show_profile_page', kwargs={'pk':self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')