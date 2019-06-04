from django.shortcuts import render, redirect
from shop.models import Item


def item_list(request):
    context = {
        # 'items': Item.objects.all(),
        'page': 'shop'
    }

    return render(request, 'shop/shop.html', context)


def product(request):

    context = {
        'page': 'shop'
    }

    return render(request, 'shop/product.html', context)


def checkout(request):

    context = {
        'page': 'cart'
    }

    return render(request, 'shop/checkout.html')
