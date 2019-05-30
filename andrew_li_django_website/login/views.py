from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from login.forms import (
    RegistrationForm, EditProfileForm
)


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

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}

        return render(request, 'login/edit_profile.html', args)


def changepassword(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')

        else:
            return redirect('changepassword')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}

        return render(request, 'login/changepassword.html', args)
