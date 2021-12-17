
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
    """This api registers a user by taking the details """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # this is the better way of writing createAPIview
    def create(self, request, *args, **kwargs):
        # the super method will send data to serializer create instance
        user = super().create(request, *args, **kwargs)
        response = dict()
        response["email"] = user.data.get('email')
        response["message"] = "User registered successfully"
        return Response(response)
    
    # Create could have been better
    # def post(self, request):
    #     response = dict()
    #     user_serializer = self.serializer_class(data=request.data, context={'request': request})
    #     user_serializer.is_valid(raise_exception=True)
    #     if user_serializer.is_valid():
    #         user = user_serializer.save()
    #         response["email"] = user.email
    #         response["message"] = "User registered successfully"
    #         return Response(response)
    #     else:
    #         return Response({"message": "invalid values entered"})
        
        
class LoginView(CreateAPIView):
    """This api logs a user into the system"""
    
    serializer_class = LoginSerializer
    
    # Exception handling and get obj or 404
    def post(self, request):
        data = request.data
        response = dict()
        try:
            user = User.objects.get(email=data["email"])
            token = Token.objects.get_or_create(user=user, )
            response["message"] = "User logged in succesfully"
            response["token"] = token[0].key
        except Exception as e:
            print("in exception")
            response["message"] = str(e)
        return Response(response) 
        
class LogoutView(APIView):
    """This api logs out a user"""
    
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
    
    # request.user.auth_token.delete()
    def get(self, request):
        request.user.auth_token.delete()
        return Response({"message": "successfully logged out"})
    
class UpdateUserData(RetrieveUpdateAPIView):
    """This api lets the currently logged in user to view and update his/her details"""
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, CustomPermission]
    
    def get_object(self):
        return self.request.user
    


    
    
    