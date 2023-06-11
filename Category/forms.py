from django import forms

from Category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['slug']

        
        