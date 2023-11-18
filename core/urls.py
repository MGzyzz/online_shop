"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from online_shop import views
from accounts.views import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('auth/login', account_views.LoginView.as_view(), name='login'),
    path('auth/logout', account_views.LogoutView.as_view(), name='logout'),
    path('product/<int:id>', views.Detail.as_view(), name='detail-views'),
    path('product/add', views.Add.as_view(), name='add-product'),
    path('product/<int:id>/edit', views.Edit.as_view(), name='edit-product'),
    path('product/<int:id>/delete', views.Delete.as_view(), name='delete-product'),
    path('product/<int:id>/add_cart', views.AddCart.as_view(), name='add-to-cart'),
    path('product/cart', views.ViewsCart.as_view(), name='cart'),
    path('product/cart/delete/<int:id>', views.DeleteProductCart.as_view(), name='delete-cart'),
    path('product/cart/add', views.CreateOrder.as_view(), name='create-order')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
