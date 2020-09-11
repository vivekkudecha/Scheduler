from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request , 'index.html')

def member_dept(request):
    return render(request, 'dept.html')

def device(request):
    return render(request, 'device.html')

def database(request):
    return render(request , 'database.html')

def payment(request):
    return render(request, 'payment.html')