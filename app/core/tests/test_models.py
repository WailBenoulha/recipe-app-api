from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTest(TestCase):
    def test_create_user(self):
        email = "test@example.com"
        password = "test0000"
        user = get_user_model.objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email,email)
        self.assertEqual(user.check_password(password))

    def test_user_email_normalized(self):
        samlpe_emails = [
            ['test1@EXAMPLE.com','test1@example.com'],
            ['test2@EXAMPLE.com','test2@example.com'],
            ['test3@EXAMPLE.com','test3@example.com'],
            ['test4@EXAMPLE.com','test4@example.com'],
        ]    
        for email, excepted in samlpe_emails:
            user = get_user_model.objects.create_user(email,'sample123')
            self.assertEqual(user.email,excepted)