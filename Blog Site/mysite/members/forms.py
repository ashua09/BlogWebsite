from dataclasses import fields
import email
from tkinter import Widget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms
from blog.models import Profile

class EditProfilePageForm(forms.ModelForm):
    
    class Meta():

        model=Profile
        fields=['bio','profile_pic','website_url','facebook_url','insta_url','linkdin_url']
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'linkdin_url':forms.TextInput(attrs={'class':'form-control'})
        }


class CreateProfilePageForm(forms.ModelForm):
    
    class Meta():

        model=Profile
        fields=['bio','profile_pic','website_url','facebook_url','insta_url','linkdin_url']
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'linkdin_url':forms.TextInput(attrs={'class':'form-control'})
        }

class SignUpForm(UserCreationForm):

    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta():
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def __init__(self, *args, **kwargs):     #for adding widget to remaining fields
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

class PasswordChangingForm(PasswordChangeForm):
    
    old_password=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2=forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta():
        model=User
        fields=['old_password','new_password1','new_password2']

class EditProfile(UserChangeForm):
 
    class Meta():
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined']
        
    def __init__(self, *args, **kwargs):
        super(EditProfile,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['last_login'].widget.attrs['class']='form-control'
        self.fields['date_joined'].widget.attrs['class']='form-control'
       
