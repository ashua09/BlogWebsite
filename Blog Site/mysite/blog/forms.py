from dataclasses import field
from logging import PlaceHolder
from tkinter import Widget
from xml.etree.ElementTree import Comment
from django import forms
from .models import Post,Category,Comment

choices=Category.objects.all().values_list('name','name')
choice_list=[]
for item in choices:
     choice_list.append(item)

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('name','body')

        widgets={
            'post':forms.Select(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }


class PostForm(forms.ModelForm):
    
    class Meta:
        model =Post
        fields = ('title','author','category','snippet','body','header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','type':'hidden', 'id':'user'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list ,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'})
        }

class EditForm(forms.ModelForm):
    
    class Meta:
        model =Post
        fields = ('title','snippet','body')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }