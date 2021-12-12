from django.http.response import Http404
from accounts.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
import json
from rest_framework import status
# Create your tests here.

class LoginApiTests(APITestCase):
    fixtures = ['dump2.json', ]
    
    def _login_user(self):
        self.user = User.objects.get(email='user@example.com')
        self.client.login(email="user@example.com", password="string")
        
    def setUp(self):
        self._login_user()
        
    def test_statistics_view(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
        response = self.client.get(reverse('statistics_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_countries_view(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
        response = self.client.get(reverse('countries_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_get_sales_view(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
        response = self.client.get(reverse('create_sales_view'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_post_sales_view(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
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
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
        response = self.client.get(reverse('sales_view', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_put_sales_view_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
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
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')
        data_post = {
                    "product": "string"
                    } 
        response = self.client.patch(reverse('sales_view',kwargs={'pk':1}), data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        
    def test_delete_sales_view_id(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token e62baa670d3b80a46afde383591eaa03de787692')  
        response = self.client.delete(reverse('sales_view',kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    
