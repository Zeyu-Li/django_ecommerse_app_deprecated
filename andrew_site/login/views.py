from django.shortcuts import render

def home(request):

    words = {"home": "Home", "text":"Hello World"}
    return render(request, 'login/home.html', context={"section": words})

# def login(request):

#     return render(request, 'login/base.html')