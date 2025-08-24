from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-select select2'}),
            'supplier': forms.Select(attrs={'class': 'form-select select2'}),
        }
