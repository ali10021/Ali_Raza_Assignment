from django.http.response import Http404
from accounts.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
import json
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
        
    def test_statistics_view(self):
        response = self.client.get(reverse('statistics_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_countries_view(self):
        response = self.client.get(reverse('countries_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_get_sales_view(self):
        response = self.client.get(reverse('create_sales_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_post_sales_view(self):
        data_post = {
            "date": "2021-12-12",
            "product": "string",
            "sales_number": 0,
            "revenue": 0,
            "user": 2
            }
        response = self.client.post(reverse('create_sales_view'), data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    
        
    def test_get_sales_view_id(self):
        response = self.client.get(reverse('sales_view', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_put_sales_view_id(self):
        data_post = {
                    "date": "2021-12-12",
                    "product": "string",
                    "sales_number": 0,
                    "revenue": 0,
                    "user": 2
                    }      
        response = self.client.put(reverse('sales_view',kwargs={'pk':1}), data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
        
    def test_patch_sales_view_id(self):
        data_post = {
                    "product": "string"
                    } 
        response = self.client.patch(reverse('sales_view',kwargs={'pk':1}), data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        
    def test_delete_sales_view_id(self):
        response = self.client.delete(reverse('sales_view',kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    
