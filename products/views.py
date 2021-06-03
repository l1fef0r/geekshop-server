import json
import os

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)



def products(request):
    context = {'title': 'Geekshop-catalog'}
    file_path = os.path.join(MODULE_DIR, 'fixtures/categories.json')
    context['categories'] = json.load(open(file_path, encoding='utf-8'))

    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context['products'] = json.load(open(file_path, encoding='utf-8'))
    return render(request, 'products/products.html', context)


def news(request):
    return render(request, 'products/news.html')


def clothes(request):
    return render(request, 'products/clothes.html')


def shoes(request):
    return render(request, 'products/shoes.html')


def features(request):
    return render(request, 'products/features.html')


def gives(request):
    return render(request, 'products/gives.html')
