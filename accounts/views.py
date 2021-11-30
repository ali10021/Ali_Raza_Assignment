
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .models import User, City
from .serializers import ( 
                          UserSerializer, 
                          LoginSerializer,
                        )
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def post(self, request):
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
        data = request.data
        try:
            user = User.objects.get(email=data["email"])
            token = Token.objects.get_or_create(user=user, )
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
        
        
# class SeeUserData(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = [IsAuthenticated, CustomPermission]
    
#     def get(self, request):
#         response = self.serializer_class(request.user, context={"request": request}).data
#         del response['password']
#         return Response(response)
    
class UpdateUserData(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        if request.user.id == pk:
            print("user matched")
            response = self.serializer_class(request.user, context={"request": request}).data
            del response['password']
            return Response(response)
        else:
            return Response({'message':"you cannot view the details or edit of another user"})

    def put(self, request, pk):
        if request.user.id == pk:
            print("user matched")
            response = self.serializer_class(request.user, context={"request": request}).data
            del response['password']
            return Response(response)
        else:
            return Response({'message':"you cannot view the details or edit of another user"})
        
    def patch(self, request, pk):
        if request.user.id == pk:
            print("user matched")
            response = self.serializer_class(request.user, context={"request": request}).data
            del response['password']
            return Response(response)
        else:
            return Response({'message':"you cannot view the details or edit of another user"})
    


    
    
    