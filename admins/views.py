from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from products.models import Product
from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from products.forms import ProductForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {'title': 'GeekShop - Admin | Users', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'title': 'GeekShop - Регистрация', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'GeekShop - Admin | update user', 'form': form, 'selected_users': selected_user,}
    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reversed('admin:admin_users'))

@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {'title': 'GeekShop - Все продукты', 'products': Product.objects.all()}
    return render(request, 'admins/admin_product_read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
        else:
            print(form.errors)
    else:
        form = ProductForm()
    context = {'title': 'GeekShop - Добавление товара', 'form': form}
    return render(request, 'admins/admin_product_create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    selected_product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES, instance=selected_product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductForm(instance=selected_product)
    context = {'title': 'GeekShop - Обновление товара', 'form': form, 'selected_product': selected_product,}
    return render(request, 'admins/admin_product_update_delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reversed('admin:admin_products'))