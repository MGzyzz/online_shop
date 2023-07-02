from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    title = forms.CharField(required=True)
    remainder = forms.IntegerField(min_value=0, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'remainder', 'price', 'img_url']