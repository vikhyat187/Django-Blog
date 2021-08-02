from os import name
from .views import UserRegisterView,UserEditView,PasswordsChangeView,PasswordsChangedView
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('register/',UserRegisterView.as_view(),name="register"),
   path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
   path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   path('password_success/',PasswordsChangedView,name="password_success"),
]