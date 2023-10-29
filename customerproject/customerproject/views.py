from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TextBox
from .forms import TextBoxForm

def homepage(request):
    return render(request, 'home.html')
    #return HttpResponse("Welcome to the Microsoft Windows Museum")

def windows95(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows95')
    return render(request, 'windows95.html', {'text_boxes': text_boxes})

def textboxForm(request):
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # Save the content to the database or perform another action
            text_box = TextBox(content=form.cleaned_data['content'])
            text_box.save()
            return redirect('name_of_the_page_to_redirect_to')

    else:
        form = TextBoxForm()

    return render(request, 'your_template_name.html', {'form': form})