from django.urls import path
from accounts.views import (
    RegisterUserView,
    LoginView,
    LogoutView,
    UpdateUserData
    )

urlpatterns = [
    path('api/v1/register/', RegisterUserView.as_view(), name="user_registration"),
    path('api/v1/login/', LoginView.as_view(), name='login_view'),
    path('api/v1/logout/', LogoutView.as_view(), name='logout_view'),
    path('api/v1/users/<int:pk>/', UpdateUserData.as_view(), name='user_update_view'),
]
