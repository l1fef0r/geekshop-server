from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)
def products(request):
    context = {
        'title': 'GeekShop',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090, 'describe': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': 23725, 'describe': 'гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390, 'describe': 'материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'черный рюкзак Nike Heritage', 'price': 2340, 'describe': 'плотная ткань. Легкий материал.'},
            {'name': 'черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590, 'describe': 'гладкий кожаный верх. Натуральный материал.'},
            {'name': 'темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890, 'describe': 'дегкая эластичная ткань сирсакер Фактурная ткань.'},
        ]
    }
    return render(request, 'products/products.html', context)
