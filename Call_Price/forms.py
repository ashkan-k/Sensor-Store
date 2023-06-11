from django import forms

from .models import CallPrice


class CallPriceForm(forms.ModelForm):
    class Meta:
        model = CallPrice
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': 'data.' + name})


class CallPriceChangeStatusForm(forms.ModelForm):
    class Meta:
        model = CallPrice
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'ng-model': name})
