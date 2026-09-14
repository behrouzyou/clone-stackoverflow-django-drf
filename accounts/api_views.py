from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import User
from rest_framework import status
from .selectors import *
from .services import *
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
class UserRegisterView(APIView):
    def post(self,request):
        serializer =UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=create_user(email=serializer.validated_data['email'],username=serializer.validated_data['username']
                         ,password=serializer.validated_data['password'])
        return Response(UserRegisterSerializer(user).data,status=status.HTTP_201_CREATED)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer =UserSerializer(request.user)
        return Response(serializer.data)

    def put(self,request):
        username = request.data.get('username')
        user=update_profile(user=request.user,username=username)
        return Response(UserSerializer(user).data)

class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request):
        serializer =ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        change_password(user=request.user,new_password=serializer.validated_data['new_password'])
        return Response({'message':'password change successfully'})

class UserDetailView(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,pk):
        user=get_user_by_id(pk)
        if not user:
            return Response({'message':'user not found'})
        serializer=UserSerializer(user)
        return Response(serializer.data)
    def delete(self,request,pk):
        user = get_user_by_id(pk)
        if not user:
            return Response({'message':'user not found'})
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UserDeactivateView(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request,pk):
        user=get_user_by_id(pk)
        if not user:
            return Response({'message':'user not found'})
        deactivate_user(user)
        return Response({'message':'user Deactivated'})
class UserActivationAccountView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,uidb64,token):
      try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=User.objects.get(pk=uid)
      except Exception:
          return Response({'message':'Invalid ling'},status=status.HTTP_400_BAD_REQUEST)
      if default_token_generator.check_token(user,token):
          user.is_active =True
          user.save(update_fields=['is_active'])
          return Response({'message':'you are activated'},status=status.HTTP_201_CREATED)
      return Response({'message': 'Invalid ling'}, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=get_user_by_mail(email=serializer.validated_data['email'])
        if user:
            reset_url=build_reset_password_link(user)
            send_reset_password_email(user=user, reset_url =reset_url)
        return Response({'message':'reset link has been sent'})
class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    def post(self,request,uidb64,token):
        serializer =ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            uid=urlsafe_base64_decode(uidb64).decode()
            user=get_user_by_id(user_id=uid)
        except Exception:
            return Response({'message':'invalid link'},status = status.HTTP_400_BAD_REQUEST)
        if not default_token_generator.check_token(user,token):
            return Response({'message': 'invalid link'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({'message': 'password change sauccessfully'})