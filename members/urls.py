from os import name
from .views import *
from django.urls import path
 
urlpatterns = [
   path('register/',UserRegisterView.as_view(),name="register")
]