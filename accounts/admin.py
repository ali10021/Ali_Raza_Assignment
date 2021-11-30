from django.contrib import admin
from accounts.models import (User,
                     Country,
                     City,)
# Register your models here.

admin.site.register(User)
admin.site.register(Country)
admin.site.register(City)
