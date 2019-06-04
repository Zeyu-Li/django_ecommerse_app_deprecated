from django.shortcuts import render, redirect
from shop.models import Item


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'shop/shop.html')


def product(request):

    return render(request, 'shop/product.html')


def checkout(request):

    return render(request, 'shop/checkout.html')
