
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts',include('accounts.urls',namespace='accounts')),
    path('answers',include('answers.urls',namespace='answers')),

    path('',include('home.urls',namespace= 'home')),
    path('questions',include('questions.urls',namespace='questions')),
]
