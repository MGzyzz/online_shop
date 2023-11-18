from django.db import models

class ItemInCart(models.Model):
    product = models.ForeignKey('online_shop.Product', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    order = models.ForeignKey('online_shop.Order', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.quantity, self.product