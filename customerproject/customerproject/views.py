from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')
    #return HttpResponse("Welcome to the Microsoft Windows Museum")

def windows95(request):
    return render(request, 'windows95.html')