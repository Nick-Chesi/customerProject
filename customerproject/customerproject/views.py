from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
    text_boxes = TextBox.objects.filter(page_identifier='windows98')
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
    text_boxes = TextBox.objects.filter(page_identifier='windowsxp')
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

def manage_textboxes(request):
    text_boxes = TextBox.objects.all()
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_textboxes')
    else:
        form = TextBoxForm()

    return render(request, 'manage_textboxes.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def edit_textbox(request, pk):
    text_box = get_object_or_404(TextBox, pk=pk)
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TextBoxForm(request.POST, instance=text_box)
            if form.is_valid():
                form.save()
                return redirect('manage_textboxes')
        elif 'delete' in request.POST:
            text_box.delete()
            return redirect('manage_textboxes')
    
    else:
        form = TextBoxForm(instance=text_box)

    return render(request, 'edit_textbox.html', {'form': form, 'text_box': text_box})
