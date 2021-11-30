from accounts.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
# Create your tests here.

class LoginApiTests(APITestCase):
    fixtures = ['db.json', ]
    
    def _login_user(self):
        print("in login")
        self.user = User.objects.get(email='1@1.com')
        print(Token.objects.all())
        self.client.login(email="1@1.com", password="1")
        print("this is self.user" , self.user)