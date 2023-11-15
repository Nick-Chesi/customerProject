from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
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

def windowsVista(request):
    text_boxes = TextBox.objects.filter(page_identifier='windowsVista')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windowsxp')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windowsVista'})
    return render(request, 'windowsVista.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def windows7(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows7')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windows7')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windows7'})
    return render(request, 'windows7.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def windows8(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows8')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windows8')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windows8'})
    return render(request, 'windows8.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def windows10(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows10')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windows10')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windows10'})
    return render(request, 'windows10.html', {
        'text_boxes': text_boxes,
        'form': form
    })

def windows11(request):
    text_boxes = TextBox.objects.filter(page_identifier='windows11')
    if request.method == 'POST':
        form = TextBoxForm(request.POST)
        if form.is_valid():
            # This will save the TextBox with the page identifier
            form.save()
            # Redirect to the same page to display the new TextBox
            return redirect('windows11')
    else:
        form = TextBoxForm(initial={'page_identifier': 'windows11'})
    return render(request, 'windows11.html', {
        'text_boxes': text_boxes,
        'form': form
    })

####################################################################
# Auth
####################################################################

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            context = {'error': 'Invalid username or password.'}
            return render(request, 'login.html', context)
    else:
        # No context is needed for a GET request to the login page.
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to a login page.
####################################################################
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


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered with an account.')
            return redirect('register')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        else:
            # Create a new superuser account for how we decided to make the accounts work
            user = User.objects.create_superuser(username=email, email=email, password=password1)
            user.save()
            messages.success(request, 'Superuser account has been created.')
            return redirect('login')

    return render(request, 'register.html')