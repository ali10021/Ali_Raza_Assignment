from rest_framework import serializers
from sales.models import(
    SalesData,
    Country
)
from django.db import models


class SalesDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SalesData
        fields = ('date', 'product', 'sales_number', 'revenue', 'user')
        
class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ('id' ,'name', 'city')