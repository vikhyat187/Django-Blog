from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm, SignUpForm,PasswordsChangeForm
from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.views import generic
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class =SignUpForm
    template_name='registration/registration.html'
    success_url=reverse_lazy('login')

class PasswordsChangeView(PasswordChangeView):
    form_class =PasswordsChangeForm
    success_url=reverse_lazy('password_success')
    
def PasswordsChangedView(request):
    return render(request,'registration/password_success.html')

class UserEditView(generic.UpdateView):
    form_class =EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user