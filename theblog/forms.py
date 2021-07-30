from django import forms
from django.db import models
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','title_tag','author','body']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'This title placeholder'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control' }),
            'author':forms.Select(attrs={'class':'form-control' }),
            'body':forms.Textarea(attrs={'class':'form-control' }),#bootstrap class form-control
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','title_tag','body']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'This title placeholder'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control' }),
            'body':forms.Textarea(attrs={'class':'form-control' }),#bootstrap class form-control
        }


