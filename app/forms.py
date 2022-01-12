# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2022-01-11 14:44:22
# @Last Modified by:   Your name
# @Last Modified time: 2022-01-11 14:56:32
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerRegistrationForm(UserCreationForm):
     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
     email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    labels = {'email': 'Email'}
    widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}     
