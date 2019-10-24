from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('Tech', 'Technology'),
    ('Access', 'Accessories'),
    ('Trans', 'Transportation'),
    ('Misc', 'Other')
)
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product", kwargs={
            "slug": self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={
            "slug": self.slug
        })


class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.items.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
