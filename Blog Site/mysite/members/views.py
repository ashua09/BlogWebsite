from urllib.request import Request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from requests import request
from .forms import SignUpForm,EditProfile,PasswordChangingForm,CreateProfilePageForm,EditProfilePageForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile

# Create your views here.
class CreateProfilePage(CreateView):
    model=Profile
    form_class=CreateProfilePageForm
    template_name='registration/create_profile_page.html'

    def form_valid(self,form):   #making the user id available for our profile so that when we save the form it save under right user
        form.instance.user=self.request.user
        return super().form_valid(form)
 
class EditProfilePage(UpdateView):
    model=Profile
    form_class=EditProfilePageForm
    template_name='registration/edit_profile_page.html'
    success_url=reverse_lazy('blog:home')

class ShowProfilePage(DetailView):
    model=Profile
    template_name='registration/profile_page.html'

    def get_context_data(self,*args, **kwargs):
        context= super(ShowProfilePage,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])        
        context['page_user']=page_user
        return context

class UserRegister(CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class UserEditProfile(UpdateView):
    form_class=EditProfile
    template_name='registration/edit_profile_setting.html'
    success_url=reverse_lazy('blog:home')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangingForm
    success_url=reverse_lazy('members:pswrd_success')   

def password_success(request):
    return render(request,'registration/pswrd_success.html')

