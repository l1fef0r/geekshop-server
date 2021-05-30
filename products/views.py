from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'products/index.html')
def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ]
    }
    return render(request, 'products/test-context.html', context)