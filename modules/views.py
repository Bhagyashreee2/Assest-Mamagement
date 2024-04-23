from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from modules.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate
from modules.renderes import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User, Asset, Transaction
from .serializers import UserSerializer, LogoutSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .serializers import LogoutSerializer
from .permissions import IsAdminOrTokenAuthenticated
from django.contrib.auth import logout as django_logout
from django.http import JsonResponse


#generate token manually 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]  #this line is to get error word while showing the errors it will be nice to see in frontend
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  #(raise_exception=True)--> the errors will be shown in postmas as usual
        user = serializer.save()
        token =get_tokens_for_user(user) #this will call the token def & generate the token
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
        # print(serializer.errors) #the erros will be shown in terminal
        

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Email = serializer.data.get('Email')
        password = serializer.data.get('password')
        user = authenticate(Email=Email, password=password)
        if user is not None:
            token =get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
    
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset link Sent, Please check your Email'}, status=status.HTTP_200_OK)
    
class UserPasswordResetView(APIView):
        renderer_classes = [UserRenderer]
        def post(self, request, uid, token, format=None):
            serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
            serializer.is_valid(raise_exception=True)
            return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
        
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'msg': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        # 1. Blacklist the refresh token
        try:
            refresh_token = request.data.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # 2. Clear session (Optional)
        django_logout(request)

        # 3. Return response
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    