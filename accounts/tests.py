from django.test import TestCase
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings
 
 
class CustomUserTest(TestCase):

    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
        })
 
        self.assertTrue(form.is_valid())
    
    def test_registration_form_fails_with_missing_password(self):
        form = UserRegistrationForm({
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'letmein1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                "please enter both passwords",
                                form.full_clean())


    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'username': 'testuser',
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())