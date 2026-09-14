
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts',include('accounts.urls',namespace='accounts')),
    path('answers',include('answers.urls',namespace='answers')),

    path('',include('home.urls',namespace= 'home')),
    path('questions',include('questions.urls',namespace='questions')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
