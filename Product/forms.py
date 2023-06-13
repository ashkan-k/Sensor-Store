from django import forms

from Product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'likes_and_dislikes']