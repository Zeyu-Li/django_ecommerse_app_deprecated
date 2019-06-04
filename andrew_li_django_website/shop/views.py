from django.shortcuts import render, redirect
from shop.models import Item
from django.views.generic import ListView, DetailView


def item_list(request):
    context = {
        'items': Item.objects.all(),
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
        'page': 'shop'
    }

    return render(request, 'shop/checkout.html', context)


class ItemsView(ListView):

    model = Item
    template_name = 'shop/shop.html'


class ItemDetailView(DetailView):

    model = Item
    template_name = 'shop/product.html'
