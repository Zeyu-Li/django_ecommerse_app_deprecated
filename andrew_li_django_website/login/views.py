from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
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


def profile(request):
    args = {'user':request.user}

    return render(request, 'login/profile.html', args)

def edit_profile(request):

    if request == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form':form}

        return render(request, 'login/edit_profile.html', args)
