from django.contrib import admin
from django.urls import path
from products.views import index, products, test_context


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', products, name='products'),
]
