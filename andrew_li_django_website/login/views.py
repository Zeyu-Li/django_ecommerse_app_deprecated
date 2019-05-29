from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from login.forms import RegistrationForm


def home(request):

    keywords = {"page": "home"}
    return render(request, 'login/home.html', keywords)


def home_redirect(request):

    return redirect('home')


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
        args = {'form':form}

        return render(request, 'login/register.html', args)
