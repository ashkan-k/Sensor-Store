from django import forms
from django.contrib.auth import get_user_model
from ContactUs.models import Suggestion, ContactUs

User = get_user_model()


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', '')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(False)
        obj.user = self.request.user
        obj.save()
        return obj


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
