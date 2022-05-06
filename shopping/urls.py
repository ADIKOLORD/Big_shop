"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from shop.views import *
from django.conf.urls.static import static
from . import settings

admin.site.site_header = 'Наша Админка'
admin.site.index_title = 'Админ Ади'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'),
    path('wishlist', wishlist, name='wishlist'),
    path('404', error, name='404'),
    path('account', account, name='account'),
    path('blog1', blog1, name='blog1'),
    path('blog2', blog2, name='blog2'),
    path('blogsingle/<int:pk>', blogsingle, name='blogsingle'),
    path('cart/', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('contact', contact, name='contact'),
    path('product/<int:category_id>', sort_product, name='sort_product'),
    path('product', product, name='product'),
    path('productdetail/<int:pk>', productdetail, name='productdetail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
