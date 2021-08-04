from os import name
from .views import ShowUserView, UserRegisterView,UserEditView,PasswordsChangeView,PasswordsChangedView,ShowUserView,EditProfilePageView,CreateProfilePageView
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
   path('register/',UserRegisterView.as_view(),name="register"),
   path('edit_profile/',UserEditView.as_view(),name="edit_profile"),
   path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   path('password_success/',PasswordsChangedView,name="password_success"),
   path('<int:pk>/profile',ShowUserView.as_view(),name="show_profile_page"),
   path('<int:pk>/edit_profile_page',EditProfilePageView.as_view(),name="edit_profile_page"),
   path('create_profile_page',CreateProfilePageView.as_view(),name="create_profile_page"),
]