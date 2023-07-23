from django.db import models
from .product import Product
from .item_in_cart import ItemInCart


class Order(models.Model):
    products = models.ManyToManyField(Product)
    username = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Username'
    )
    number_phone = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        verbose_name='Number Phone'
    )

    address = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Address'
    )

    date_and_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username