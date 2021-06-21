from django.urls import path

from admins.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    ProductCreateView, ProductDeleteView, ProductUpdateView, ProductListView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products', ProductListView, name='admin_products'),
    path('products/create/', ProductCreateView, name='admin_products_create'),
    path('products/update/<int:pk>/', ProductUpdateView, name='admin_products_update'),
    path('products/delete/<int:pk>/', ProductDeleteView, name='admin_products_delete'),
]
