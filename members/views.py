from django.views.generic.edit import CreateView
from theblog.models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm, SignUpForm,PasswordsChangeForm,ProfilePageForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from theblog.models import Profile
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class =SignUpForm
    template_name='registration/registration.html'
    success_url=reverse_lazy('login')

class ShowUserView(DetailView):
    model=Profile
    template_name='registration/user_profile.html'
    success_url=reverse_lazy('home')
    

    def get_context_data(self, *args,**kwargs):
        context= super(ShowUserView,self).get_context_data(*args,**kwargs)
        page_user= get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user']=page_user
        return context    

class PasswordsChangeView(PasswordChangeView):
    form_class =PasswordsChangeForm
    success_url=reverse_lazy('password_success')

class CreateProfilePageView(CreateView):
    model=Profile
    form_class=ProfilePageForm
    template_name="registration/create_user_profile_page.html"
    
    def form_valid(self,form):
        form.instance.user=self.request.user#saving the user id on the form
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model=Profile
    template_name='registration/edit_profile_page.html'
    fields=['bio','profile_pic','website_url','twitter_url','instagram_url','fb_url','pinterest_url']
    success_url=reverse_lazy('home')
    
def PasswordsChangedView(request):
    return render(request,'registration/password_success.html')

class UserEditView(generic.UpdateView):
    form_class =EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user