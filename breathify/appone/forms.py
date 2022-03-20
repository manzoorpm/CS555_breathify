import email
from tkinter import Widget
from unicodedata import name
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class userform(UserCreationForm): #Form for user login
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "login-field w-input", "placeholder": "Username", "maxlength": "256", "name": "username", "id":"username"}))
	email = forms.CharField(widget=forms.EmailInput(attrs={"class": "login-field w-input", "placeholder": "Email", "maxlength": "256", "name": "email", "id":"email"}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "login-field w-input", "placeholder": "Password", "maxlength": "256", "name": "password1", "id":"password1"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "login-field w-input", "placeholder": "Retype Password", "maxlength": "256", "name": "password2", "id":"password2"}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']