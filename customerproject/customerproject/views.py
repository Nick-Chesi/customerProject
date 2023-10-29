from django.http import HttpResponse
from django.shortcuts import render
from .models import TextBox

def homepage(request):
    return render(request, 'home.html')
    #return HttpResponse("Welcome to the Microsoft Windows Museum")

def windows95(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows95')
    return render(request, 'windows95.html', {'text_boxes': text_boxes})