from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone


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


@login_required
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


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.items.create(item=item)
    order_qs = Order.items.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # checks if order is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect("product", slug=slug)
        else:
            order.items.add(order_item)
            return redirect("product", slug=slug)

    else:
        ordered_date = timezone.now()
        order = Order.items.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("product", slug=slug)
