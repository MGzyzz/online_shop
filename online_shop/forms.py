from django import forms
from online_shop.models.product import Product
from online_shop.models.item_in_cart import ItemInCart
from online_shop.models.order import Order


class ProductForms(forms.ModelForm):
    title = forms.CharField(required=True)
    remainder = forms.IntegerField(min_value=0, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'remainder', 'price', 'img_url']



class SearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        required=False,
        label='Найти',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'enter search value'
        })
    )


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = ItemInCart
        fields = ['product', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['id', 'username', 'number_phone', 'address']

        products = forms.ModelMultipleChoiceField(
            queryset=ItemInCart.objects.all(),
            required=True
        )