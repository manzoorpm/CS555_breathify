from tkinter import Widget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from appone.models import *


class userform(UserCreationForm): #Form for user login
	username = forms.CharField(widget=forms.TextInput(attrs={"class": "login-field w-input", "placeholder": "Username", "maxlength": "256", "name": "username", "id":"username"}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "login-field w-input", "placeholder": "Firstname", "maxlength": "256", "name": "firstname", "id":"firstname"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "login-field w-input", "placeholder": "Lastname", "maxlength": "256", "name": "lastname", "id":"lastname"}))
	email = forms.CharField(widget=forms.EmailInput(attrs={"class": "login-field w-input", "placeholder": "Email", "maxlength": "256", "name": "email", "id":"email"}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "login-field w-input", "placeholder": "Password", "maxlength": "256", "name": "password1", "id":"password1"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "login-field w-input", "placeholder": "Retype Password", "maxlength": "256", "name": "password2", "id":"password2"}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class scoreForm(ModelForm):

	user = forms.CharField(widget=forms.HiddenInput(attrs={"name": "user" , "id": "user", "value": "default"}))
	game_level = forms.CharField(widget=forms.HiddenInput(attrs={"name": "levelNameForm" , "id": "levelNameForm", "value": "default"}))
	activity_points = forms.CharField(widget=forms.HiddenInput(attrs={"name": "latestScoreForm" , "id": "latestScoreForm", "value": "default"}))

	class Meta:
		model = activity
		fields = ['user', 'game_level', 'activity_points']