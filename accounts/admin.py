from django.contrib import admin
from .models import (User,
                     Country,
                     City,
                     SalesData)
# Register your models here.

admin.site.register(User)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(SalesData)
