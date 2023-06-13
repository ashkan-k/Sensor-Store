from django import forms

from Product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "slug", "short_text",
                  "text", "tags", "tags", "price", "status", "count", "suggestion_count", "original_image", "user", "category"]
