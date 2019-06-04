from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

CATEGORY_CHOICES = (
    ('Tech','Technology'),
    ('Access', 'Accessories'),
    ('Trans', 'Transportation'),
    ('Misc','Other')
)
LABEL_CHOICES = (
    ('N','new'),
    ('H', 'hot'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    order = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
