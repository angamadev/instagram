from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestHomeViews(TestCase):
    
    # Creo un usuario
    def setUp(self):
        self.user = User.objects.create_user(
        username = 'test',
        password = 'test',
        first_name = 'Andres',
        last_name = 'Garcia Marquez',
        email = 'agm@agm.com',
        )
        self.profile = UserProfile.objects.create(user=self.user)
        
    # Chequeo las vistas del core
    def test_home_views(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_registro_views(self):
        url = reverse('registro')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_logout_views(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_contacto_views(self):
        url = reverse('contacto')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class TestCreateUser(TestCase):
    
    def setUp(self):
        # Creo 2 usuarios y 2 perfiles
        self.user1 = User.objects.create_user(username='Ancor',password='0012')
        self.user2 = User.objects.create_user(username='Carlos',password='0012')
        self.profile1 = UserProfile.objects.create(user=self.user1,bio='Hijo pequeño')
        self.profile2 = UserProfile.objects.create(user=self.user2,bio='Hijo grande')
        
        
    def test_create_user(self):
        # Miro si se crearon bien los 2 usuarios comparandolos con su bio
        self.assertEqual(self.profile1.bio, "Hijo pequeño")
        self.assertEqual(self.profile2.bio, "Hijo grande")
        
