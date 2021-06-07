from django.contrib import admin
from django.urls import path, include
from products.views import index, news, clothes, gives, features, shoes

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),

    path('news/', news, name='news'),
    path('shoes/', shoes, name='shoes'),
    path('clothes/', clothes, name='clothes'),
    path('gives/', gives, name='gives'),
    path('features/', features, name='features'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
