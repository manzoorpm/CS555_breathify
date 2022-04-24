from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from appone. models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.signin_url = reverse('signin')
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')  
        self.registration_url = reverse('registration')
        self.home_url = reverse('home')
        self.levelone_url = reverse('levelone')
        self.leveltwo_url = reverse('leveltwo')
        self.levelthree_url = reverse('levelthree')
        self.levelfour_url = reverse('levelfour')
        self.levelfive_url = reverse('levelfive')
        self.levelsix_url = reverse('levelsix')
        self.levelangry_url = reverse('levelangry')
        self.leveldepressed_url = reverse('leveldepressed')
        self.levelstressed_url = reverse('levelstressed')
        self.levelrelief_url = reverse('relief')
        self.profile_url = reverse('profile')

    def test_sign_in_GET(self):
        response = self.client.get(self.signin_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appone/signin.html')
    
    def test_registration_GET(self):
        response = self.client.get(self.registration_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appone/registration.html')

    def test_home_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_levelone_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelone_url)
        self.assertEqual(response.status_code, 200)
    
    def test_leveltwo_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.leveltwo_url)
        self.assertEqual(response.status_code, 200)
    
    def test_levelthree_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelthree_url)
        self.assertEqual(response.status_code, 200)
    
    def test_levelfour_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelfour_url)
        self.assertEqual(response.status_code, 200)
    
    def test_levelfive_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelfive_url)
        self.assertEqual(response.status_code, 200)
    
    def test_levelsix_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelsix_url)
        self.assertEqual(response.status_code, 200)

    def test_levelangry_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelangry_url)
        self.assertEqual(response.status_code, 200)
    
    def test_leveldepressed_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.leveldepressed_url)
        self.assertEqual(response.status_code, 200)

    def test_levelstressed_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelstressed_url)
        self.assertEqual(response.status_code, 200)
    
    def test_levelrelief_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.levelrelief_url)
        self.assertEqual(response.status_code, 200)
    
    def test_profile_GET(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
    
    
   
    
    

