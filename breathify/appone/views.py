from http.server import ThreadingHTTPServer
from itertools import product
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *

def home(request):
	
	return render(request, 'appone/registration.html')