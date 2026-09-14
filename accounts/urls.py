from django.urls import path
from rest_framework.authtoken import views as token_views
from . import views, api_views


app_name = 'accounts'
urlpatterns = [
    path('register/',api_views.UserRegisterView.as_view(),name='user_register'),
    path('api_token',token_views.obtain_auth_token),
    path('profile/',api_views.UserProfileView.as_view()),
    path('change-password/',api_views.UserChangePasswordView.as_view()),
    path('admin/<int:pk>/',api_views.UserDetailView.as_view()),
    path('admin/<int:pk>/deactivate/',api_views.UserDeactivateView.as_view()),
    path('activate/<uidb64>/<token>/',api_views.UserActivationAccountView.as_view()),
    path('forget-password/',api_views.ForgotPasswordView.as_view()),
    path('reset-password/<uidb64>/<token>/',api_views.ResetPasswordView.as_view()),
]