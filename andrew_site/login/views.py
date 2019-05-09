from django.shortcuts import render
from django.template import loader 

def home(request):

    template = loader.get_template('home.html')
    context = {

        'name': 'Home',

    }
    return render(request, '')
