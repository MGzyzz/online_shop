from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .forms import ProductForms


# Create your views here.


def home(request):
    return render(request, 'home.html', context={'products': Product.objects.order_by('category', 'title'), 'form': form})


def detail_views_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    else:
        return render(request, 'product_detail.html', context={'product': product})


def add_product(request):
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('detail-views', id=product.id)
    else:
        form = ProductForms
    return render(request, 'add_product.html', {'form': form, 'category': Category.objects.all()})


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        form = ProductForms(instance=product)
        return render(request, 'edit_product.html', {'product': product, 'category': Category.objects.all(), 'form': form})
    elif request.method == 'POST':
        form = ProductForms(data=request.POST, instance=product)
        if form.is_valid():
            product.save()
            return redirect('detail-views', id=product.id)
        else:
            print('not work')
            return render(request, 'edit_product.html', {'product': product, 'category': Category.objects.all(), 'form': form})

