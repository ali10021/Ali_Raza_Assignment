from django.urls import path
from sales.views import (
    Statistics,
    SalesView,
    CreateSalesView,
    ListCountries,
    )

urlpatterns = [
    path('api/v1/sales_statistics/', Statistics.as_view(), name='statistics_view'),
    path('api/v1/sales/<int:pk>/', SalesView.as_view(), name='sales_view'),
    path('api/v1/sales/', CreateSalesView.as_view(), name='create_sales_view'),
    path('api/v1/countries/', ListCountries.as_view(), name='countries_view'),
]
