from django.db import models
from .product import Product


class ItemInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')

    def __str__(self):
        return self.quantity