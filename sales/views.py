
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from sales.models import SalesData
from accounts.models import Country
from .serializers import ( 
                          SalesDataSerializer,
                          CountrySerializer
                        )
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .utils import calculate_average_sales, calculate_average_sales_for_all_users, customResponse
from django.db.models import Max

# Create your views here.
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

    def get(self, request, pk):
        sales_data = SalesData.objects.get(pk=pk)
        if request.user.id == sales_data.user.id:
            print("user matched")
            response = self.serializer_class(sales_data, context={"request": request}).data
            return Response(response)
        else:
            return Response({'message':"you cannot view the details or edit of another user"})

    def put(self, request, pk):      
        sales_data = SalesData.objects.get(pk=pk)
        if request.user.id == sales_data.user.id:
            print("user matched")
            response = self.serializer_class(request.data, context={"request": request}).data
            return Response(response)
        else:
            return Response({'message':"you cannot view the details or edit of another user"})
        
    def patch(self, request, pk): 
        sales_data = SalesData.objects.get(pk=pk)
        if request.user.id == sales_data.user.id:
            print("user matched")
            response = self.serializer_class(request.data, context={"request": request}).data
            return Response(response)
        else:
            return Response({'message':"you cannot view the details or edit of another user"})
    

class CreateSalesView(ListCreateAPIView):
    queryset = SalesData.objects.all()
    serializer_class = SalesDataSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        if request.user.id == request.data['user']:
            print("user matched")
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response({'message':"you cannot view the details or edit of another user"})
    
class ListCountries(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]