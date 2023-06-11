from django import forms

from Cart.models import Cart


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(False)
        obj.user = self.request.user
        obj.save()
        return obj
