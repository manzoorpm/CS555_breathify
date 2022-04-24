from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .forms import userform, scoreForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django.conf import settings
from django.db.models import Sum


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
def relief(request):
	context = {}
	return render(request, 'appone/relief_home.html')

@login_required(login_url='signin') #redirect to login if not 
def levelone(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'appone/levelone.html', context)

@login_required(login_url='signin') #redirect to login if not 
def leveltwo(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'appone/leveltwo.html', context)

@login_required(login_url='signin') #redirect to login if not 
def levelthree(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'appone/levelthree.html', context)

@login_required(login_url='signin') #redirect to login if not 
def levelfour(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'appone/levelfour.html', context)

@login_required(login_url='signin') #redirect to login if not 
def levelfive(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'appone/levelfive.html', context)

@login_required(login_url='signin') #redirect to login if not 
def levelsix(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form': form}
	return render(request, 'appone/levelsix.html', context)


@login_required(login_url='signin') #redirect to login if not 
def levelangry(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('relief')
	context = {'form': form}
	return render(request, 'appone/levelangry.html', context)

@login_required(login_url='signin') #redirect to login if not 
def leveldepressed(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('relief')
	context = {'form': form}
	return render(request, 'appone/leveldepressed.html', context)

@login_required(login_url='signin') #redirect to login if not 
def levelstressed(request):
	form = scoreForm()
	if request.method == 'POST':
		form = scoreForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('relief')
	context = {'form': form}
	return render(request, 'appone/levelstressed.html', context)

@login_required(login_url='signin') #redirect to login if not 
def profile(request):
	username = request.user
	emailId = username.email
	firstName = username.first_name
	lastName = username.last_name

	activity_data = activity.objects.filter(user=username)
	totalPoints = activity.objects.filter(user=username).aggregate(Sum('activity_points'))
	totalPointSum = totalPoints['activity_points__sum']

	context = {
		'user': username,
		'email': emailId,
		'first':firstName,
		'last':lastName,
		'activitys': activity_data,
		'totalPoints': totalPointSum
	}
	return render(request, 'appone/profile.html', context)
