from base64 import urlsafe_b64encode
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appone.views import *

class Test_signin_url(SimpleTestCase):

    def test_signin_url_is_resolved(self):
        url = reverse('signin')
        self.assertEqual(resolve(url).func, signin)

class Test_registration_url(SimpleTestCase):

    def test_lregistration_url_is_resolved(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration)
    
class Test_home_url(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

class Test_signout_url(SimpleTestCase):

    def test_signout_url_is_resolved(self):
        url = reverse('signout')
        self.assertEqual(resolve(url).func, signout)

class Test_levelone_url(SimpleTestCase):

    def test_levelone_url_is_resolved(self):
        url = reverse('levelone')
        self.assertEqual(resolve(url).func, levelone)

class Test_leveltwo_url(SimpleTestCase):

    def test_leveltwo_url_is_resolved(self):
        url = reverse('leveltwo')
        self.assertEqual(resolve(url).func, leveltwo)

class Test_levelthree_url(SimpleTestCase):

    def test_levelthree_url_is_resolved(self):
        url = reverse('levelthree')
        self.assertEqual(resolve(url).func, levelthree)

class Test_levelfour_url(SimpleTestCase):

    def test_levelfour_url_is_resolved(self):
        url = reverse('levelfour')
        self.assertEqual(resolve(url).func, levelfour)