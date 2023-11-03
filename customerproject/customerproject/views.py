from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TextBox
from .forms import TextBoxForm

def homepage(request):
    return render(request, 'home.html')
    #return HttpResponse("Welcome to the Microsoft Windows Museum")

# Page ID is for the individual textbox models

def windows95(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows95')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windows95')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windows95'})
    return render(request, 'windows95.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def windows98(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows95')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windows98')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windows98'})
    return render(request, 'windows98.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def windowsxp(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows95')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windowsxp')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windowsxp'})
    return render(request, 'windowsxp.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def textboxForm(request):
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # Save the content to the database or perform another action
            text_box = TextBox(content=form.cleaned_data['content'])
            text_box.save()
            return redirect('')

    else:
        form = TextBoxForm()

    return render(request, 'base.html', {'form': form})