from django import forms
from django.contrib.auth.hashers import check_password

from .models import bbs

class BoardForm(forms.ModelForm):
    class Meta:
        model = bbs
        fields = ['title', 'writer', 'content']
        widgets ={
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'writer' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }
