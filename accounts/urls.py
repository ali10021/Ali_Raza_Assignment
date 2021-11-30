from django.urls import path
from accounts.models import SalesData
from accounts.views import (
    index,
    RegisterUserView,
    LoginView,
    LogoutView,
    updateSalesData,
    Statistics,
    ListLoggedInUser,
    SalesView,
    CreateSalesView,
    ListCountries,
    SeeAndUpdateUserData
    )

urlpatterns = [
    path('api/v1/indexview/', index.as_view(), name="index"),
    path('api/v1/register/', RegisterUserView.as_view(), name="user_registration"),
    path('api/v1/login/', LoginView.as_view(), name='login_view'),
    path('api/v1/logout/', LogoutView.as_view(), name='logout_view'),
    path('api/v1/users/<int:pk>/', SeeAndUpdateUserData.as_view(), name='user_view'),
    path('api/v1/list_logged_in_user/', ListLoggedInUser.as_view(), name='list_logged_in_user_view'),
    path('api/v1/update-sales-data/<int:pk>/', updateSalesData.as_view(), name='sales_data_view'),
    path('api/v1/sales_statistics/', Statistics.as_view(), name='statistics_view'),
    path('api/v1/sales/<int:pk>/', SalesView.as_view(), name='sales_view'),
    path('api/v1/sales/', CreateSalesView.as_view(), name='create_sales_view'),
    path('api/v1/countries/', ListCountries.as_view(), name='countries_view'),
]
