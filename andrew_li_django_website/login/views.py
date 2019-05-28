from django.shortcuts import render


def home(request):

    keywords = {"text": "Login Project:", "page": "home"}
    return render(request, 'login/home.html', keywords)
