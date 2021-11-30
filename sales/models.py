from django.db import models
from baseModel.base_model import BaseModel
from accounts.models import User

# Create your models here.

class Country(BaseModel):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)
    
class City(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='city')
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.name)

class SalesData(BaseModel):
    date = models.DateField()
    product = models.CharField(max_length=200)
    sales_number = models.IntegerField()
    revenue = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales_data')
    
    def __str__(self):
        return str(self.user.email)