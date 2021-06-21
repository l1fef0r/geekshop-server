from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from products.models import Product
from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from products.forms import ProductForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {'title': 'GeekShop - Admin | Users', 'users': User.objects.all()}
#     return render(request, 'admins/admin-users-read.html', context)

class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Админ | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {'title': 'GeekShop - Регистрация', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'GeekShop - Admin | update user', 'form': form, 'selected_users': selected_user,}
#     return render(request, 'admins/admin-users-update-delete.html', context)

class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reversed('admin:admin_users'))
class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin_product_read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Все продукты'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#     context = {'title': 'GeekShop - Все продукты', 'products': Product.objects.all()}
#     return render(request, 'admins/admin_product_read.html', context)
class ProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin_product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('admins:admin_products')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProductForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductForm()
#     context = {'title': 'GeekShop - Добавление товара', 'form': form}
#     return render(request, 'admins/admin_product_create.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin_product_update_delete.html'

    selected_product = Product.objects.get(id=id)

    form_class = ProductForm
    success_url = reverse_lazy('admins:admin_products')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_update(request, id):
#     selected_product = Product.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProductForm(data=request.POST, files=request.FILES, instance=selected_product)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductForm(instance=selected_product)
#     context = {'title': 'GeekShop - Обновление товара', 'form': form, 'selected_product': selected_product,}
#     return render(request, 'admins/admin_product_update_delete.html', context)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin_product_update_delete.html'
    success_url = reverse_lazy('admins:admin_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_products_delete(request, id):
#     product = Product.objects.get(id=id)
#     product.is_active = False
#     product.save()
#     return HttpResponseRedirect(reversed('admin:admin_products'))