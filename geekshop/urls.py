from django.contrib import admin
from django.urls import path
from products.views import index, products, news, clothes, gives, features, shoes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('news/', news, name='news'),
    path('shoes/', shoes, name='shoes'),
    path('clothes/', clothes, name='clothes'),
    path('gives/', gives, name='gives'),
    path('features/', features, name='features'),
]
