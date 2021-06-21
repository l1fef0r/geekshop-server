
from django.forms import ModelForm, TextInput, FileInput
from products.models import Product

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'category',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control py-4', 'readonly': False}),
            'image': FileInput(attrs={'class': 'custom-file-input'}),
            'description': TextInput(attrs={'class': 'form-control py-4', 'readonly': False}),
            'price': TextInput(attrs={'class': 'form-control py-4', 'readonly': False}),
            'category': TextInput(attrs={'class': 'form-control py-4', 'readonly': False}),
        }