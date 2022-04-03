from base64 import urlsafe_b64encode
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appone.views import signin, registration

class Test_signin_url(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('signin')
        self.assertEqual(resolve(url).func, signin)

class Test_registration_url(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration)
    
