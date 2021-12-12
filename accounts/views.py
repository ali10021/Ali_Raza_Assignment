
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
from .permissions import CustomPermission

# Create your views here.

class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    def post(self, request):
        response = dict()
        user_serializer = self.serializer_class(data=request.data, context={'request': request})
        user_serializer.is_valid(raise_exception=True)
        if user_serializer.is_valid():
            user = user_serializer.save()
            response["email"] = user.email
            response["message"] = "User registered successfully"
            return Response(response)
        else:
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
    
class UpdateUserData(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, CustomPermission]
    
    def get_object(self):
        return self.request.user
    


    
    
    