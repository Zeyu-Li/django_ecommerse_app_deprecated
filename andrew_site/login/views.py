from django.shortcuts import render

def home(request):

    words = {"home": "Home", "text":"Login Project:", "link":"login.html"}
    return render(request, 'login/home.html', context={"section": words})

def login(request):

    return render(request, 'login/login.html')