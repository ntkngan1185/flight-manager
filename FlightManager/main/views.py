from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Authenticate
def signup(request):
    return render(request, 'accounts/signup.html')

def home(request):
    return render(request, 'accounts/dashboard/dashboard.html')

def flights(request):
    return render(request, 'accounts/flights.html')

def customer(request):
    return render(request, 'accounts/customer.html')