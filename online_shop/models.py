from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name = 'Category'
    )


class Product(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Title'
    )
    description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name='Description'
    )
    img_url = models.CharField(
        max_length=5000,
        verbose_name='Image'
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    remainder = models.IntegerField(
        verbose_name='Remainder'
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Price'
    )