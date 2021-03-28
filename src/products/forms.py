from django import forms

from .models import Product

class ProductModelForm(forms.ModelForm):
    # django forms unleashed
    class Meta:
        model = Product
        fields = [
            'title',
            'slug'
        ]