from django.core.checks import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import urlencode
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from online_shop.models.product import Category, Product
from .forms import ProductForms, SearchForm, AddToCartForm, OrderForm
from online_shop.models.item_in_cart import ItemInCart
from online_shop.models.order import Order
# Create your views here.


class Home(ListView):
    template_name = 'home.html'
    context_object_name = 'products'
    model = Product
    ordering = ['title']
    paginate_by = 10


    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value)
            qs = qs.filter(query)

        return qs

    def get_allow_empty(self):
        allow_empty = True
        return allow_empty

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search_query')



class Detail(DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'id'


class Add(CreateView):
    template_name = 'add_card.html'
    model = Product
    form_class = ProductForms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_success_url(self):
        product_id = self.object.pk
        return reverse_lazy('detail-views', kwargs={'id': product_id})


class Edit(UpdateView):
    model = Product
    template_name = 'edit_product.html'
    form_class = ProductForms
    context_object_name = 'product'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('detail-views', kwargs={'id': self.object.id})



class Delete(DeleteView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'



class AddCart(CreateView):
    form_class = AddToCartForm
    template_name = 'add_product_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['id']
        product = get_object_or_404(Product, id=product_id)
        context['product'] = product
        return context

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['id'])
        quantity = form.cleaned_data['quantity']

        cart_item, created = ItemInCart.objects.get_or_create(product=product)

        if created:
            cart_item.quantity = min(quantity, product.remainder)
        else:
            cart_item.quantity = min(cart_item.quantity + quantity, product.remainder)

        cart_item.save()

        return redirect('home')

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        print(form.errors)
        return redirect('home')


class ViewsCart(ListView):
    template_name = 'views_card.html'
    model = ItemInCart
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = ItemInCart.objects.all()
        total_sum = sum(item.product.price * item.quantity for item in cart)
        context['total_sum'] = total_sum
        context['order'] = OrderForm
        return context


class DeleteProductCart(DeleteView):
    template_name = 'views_card.html'
    model = ItemInCart
    context_object_name = 'cart'
    success_url = reverse_lazy('cart')
    pk_url_kwarg = 'id'


class CreateOrder(CreateView):
    template_name = 'views_card.html'
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.save()

        car_item = ItemInCart.objects.all()
        for item in car_item:
            order.products.add(item.product, item.quantity)
        car_item.delete()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('cart')