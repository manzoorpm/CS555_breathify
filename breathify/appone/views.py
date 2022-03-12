from http.server import ThreadingHTTPServer
from itertools import product
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *

def signin(request):
	
	return render(request, 'appone/sign_in.html')