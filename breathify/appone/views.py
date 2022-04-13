from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .forms import userform
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.conf import settings


def signin(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'appone/signin.html', context)

def signout(request):
	logout(request)
	return redirect('signin')


def registration(request):
	
	form = userform()

	if request.method == 'POST':
		form = userform(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('signin')

	context = {'form': form}
	return render(request, 'appone/registration.html', context)

@login_required(login_url='signin') #redirect to login if not 
def home(request):
	context = {}
	return render(request, 'appone/home.html')

@login_required(login_url='signin') #redirect to login if not 
def levelone(request):
	context = {}
	return render(request, 'appone/levelone.html')

@login_required(login_url='signin') #redirect to login if not 
def leveltwo(request):
	context = {}
	return render(request, 'appone/leveltwo.html')

@login_required(login_url='signin') #redirect to login if not 
def levelthree(request):
	context = {}
	return render(request, 'appone/levelthree.html')

@login_required(login_url='signin') #redirect to login if not 
def levelfour(request):
	context = {}
	return render(request, 'appone/levelfour.html')

@login_required(login_url='signin') #redirect to login if not 
def profile(request):
	context = {}
	return render(request, 'appone/profile.html')

def update_user(request, pk):

	user = settings.objects.get(id=pk)
	form = userForm(instance=user)

	if request.method == 'POST':
		form = userForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/user_profile.html', context)