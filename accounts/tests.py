from django.http.response import Http404
from accounts.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
# Create your tests here.

class LoginApiTests(APITestCase):
    fixtures = ['dump.json', ]
    
    def _login_user(self):
        self.user = User.objects.get(email='user2@example.com')
        login = self.client.login(email="user2@example.com", password="string")
        # now the auth header is set for all requests
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user.auth_token.key)
        self.assertTrue(login)
        
    def setUp(self):
        self._login_user()
        
    def test_register_user(self):
        data_post = {
                    "email": "user@example3.com",
                    "password": "string",
                    "confirmPassword": "string",
                    "name": "string",
                    "gender": "MALE",
                    "age": 0,
                    "city": 1
                    }
        response = self.client.post(reverse('user_registration'), data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    def test_get_profile(self):
        self.client.login(email="user2@example.com", password="string")
        response = self.client.get(reverse('user_update_view'))
        self.assertEqual(response.data.get('email'), "user2@example.com")
        
    def test_put_details(self):
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
        data_put = {
                    "email": "user@example3.com",
                    "password": "string",
                    "confirmPassword": "string",
                    "name": "string",
                    "gender": "MALE",
                    "age": 0,
                    "city": 1
                    }
        response = self.client.put(reverse('user_update_view'), data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_patch_details(self):
        data_patch = {
                    "gender": "MALE"   
                    }
        response = self.client.patch(reverse('user_update_view'), data_patch)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    