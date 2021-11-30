from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from baseModel.base_model import BaseModel
from .choices import GenderEnum
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Country(BaseModel):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)
    
class City(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='city')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)
    

class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    gender = models.CharField(max_length=200, choices=GenderEnum.choices())
    age = models.IntegerField(null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='user', default="", null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class SalesData(BaseModel):
    date = models.DateField()
    product = models.CharField(max_length=200)
    sales_number = models.IntegerField()
    revenue = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales_data')
    
    def __str__(self):
        return str(self.user.email)