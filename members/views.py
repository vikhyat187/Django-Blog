from .forms import SignUpForm
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class =SignUpForm
    template_name='registration/registration.html'
    success_url=reverse_lazy('login')
