from django.urls import path
from . import views, api_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


app_name = 'accounts'
urlpatterns = [
    path('register/',api_views.UserRegisterView.as_view(),name='user_register'),

    path('profile/',api_views.UserProfileView.as_view()),
    path('change-password/',api_views.UserChangePasswordView.as_view()),
    path('admin/<int:pk>/',api_views.UserDetailView.as_view()),
    path('admin/<int:pk>/deactivate/',api_views.UserDeactivateView.as_view()),
    path('activate/<uidb64>/<token>/',api_views.UserActivationAccountView.as_view()),
    path('forget-password/',api_views.ForgotPasswordView.as_view()),
    path('reset-password/<uidb64>/<token>/',api_views.ResetPasswordView.as_view()),
    path("login/", api_views.UserLoginView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]