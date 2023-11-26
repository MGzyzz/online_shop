from django.urls import path
from online_shop.views import *

urlpatterns = [
    path('<int:id>/', Detail.as_view(), name='detail-views'),
    path('add/', Add.as_view(), name='add-product'),
    path('<int:id>/edit/', Edit.as_view(), name='edit-product'),
    path('<int:id>/delete/', Delete.as_view(), name='delete-product'),
    path('<int:id>/add_cart/', AddCart.as_view(), name='add-to-cart'),
    path('cart/', ViewsCart.as_view(), name='cart'),
    path('cart/delete/<int:id>/', DeleteProductCart.as_view(), name='delete-cart'),
    path('cart/add/', CreateOrder.as_view(), name='create-order')
]