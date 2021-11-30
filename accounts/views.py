from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Country, User, City, SalesData
from .serializers import ( 
                          UserSerializer, 
                          LoginSerializer,
                          SalesDataSerializer,
                          CountrySerializer
                        )
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .utils import calculate_average_sales, calculate_average_sales_for_all_users, customResponse
from django.db.models import Max


# Create your views here.

class index(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        print("itm ")
        return HttpResponse("hello its me babe")



class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def post(self, request):
        print("im in post")
        response = dict()
        city_obj = City.objects.get(name=request.data['city'])
        request.data['city'] = city_obj.id
        print(request.data)
        user_serializer = self.serializer_class(data=request.data, context={'request': request})
        # write the following line to know any error occurring due to valid data not being passed to serializer
        user_serializer.is_valid(raise_exception=True)
        if user_serializer.is_valid():
            user = user_serializer.save()
            response["email"] = user.email
            response["message"] = "User registered successfully"
            return Response(response)
        else:
            print(user_serializer.data)
            return Response({"message": "invalid values entered"})
        
        
class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        print("in post")
        data = request.data
        try:
            user = User.objects.get(email=data["email"])
            token = Token.objects.get_or_create(user=user, )
            print(token[0].key)
            print(request.user)
            response = dict()
            response["message"] = "User logged in succesfully"
            response["token"] = token[0].key
            return Response(response)
        except Exception as e:
            print(e)
            
        
class LogoutView(APIView):

    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"message": "successfully logged out"})
        
        
class ListLoggedInUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            logged_user = User.objects.get(email=request.user.email)
            if logged_user:
                response = self.serializer_class(logged_user, context={"request": request}).data
                del response['password']
            return Response(response)
        except Exception as e:
            return Response(e)
        
class SeeAndUpdateUserData(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

class updateSalesData(RetrieveUpdateAPIView):
    queryset = SalesData.objects.all()
    serializer_class = SalesDataSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    

class Statistics(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        custom_response = customResponse()
        sales_data = SalesData.objects.filter(user=request.user)
        sales_data_all_user = SalesData.objects.all()
        max_revenue = SalesData.objects.filter(user=request.user).values('sales_number').annotate(Max('revenue'))
        product_highest_revenue_for_current_user = SalesData.objects.filter(user=request.user).values('product').annotate(Max('revenue'))
        product_highest_sales_number_for_current_user = SalesData.objects.filter(user=request.user).values('product').annotate(Max('sales_number'))
        average_sales = calculate_average_sales(sales_data)
        average_sales_all_user = calculate_average_sales_for_all_users(sales_data_all_user)
        custom_response.addKey("average_sales", average_sales)
        custom_response.addKey("average_sales_all_users", average_sales_all_user)
        custom_response.addKey("highest_revenue_sale_for_current_user", max_revenue)
        custom_response.addKey("product_highest_revenue_for_current_user", product_highest_revenue_for_current_user)
        custom_response.addKey("product_highest_sales_number_for_current_user", product_highest_sales_number_for_current_user)
        return Response(custom_response.getResponse())
    
class SalesView(RetrieveUpdateDestroyAPIView):
    queryset = SalesData.objects.all()
    serializer_class = SalesDataSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    

class CreateSalesView(ListCreateAPIView):
    queryset = SalesData.objects.all()
    serializer_class = SalesDataSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
class ListCountries(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    
    