from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models import Q
from django.contrib import messages
from Auth.models import Code
from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS
from User.helpers import check_user_exist

User = get_user_model()


class UserSimpleForm(forms.ModelForm):
    password2 = forms.CharField(
        max_length=100, required=True, widget=forms.PasswordInput(), label='تکرار رمز عبور')

    class Meta:
        model = User
        fields = ['username', 'phone', 'password']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError('رمز عبور با تکرار آن مغایرت دارد!')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.pop('password', None)
        if password:
            user.set_password(password)
        if commit:
            user.save()

        code = Code.objects.create_new_code(user)
        self.request.session['verify_phone'] = user.phone
        messages.success(
            self.request, 'ثبت نام شما با موفقیت انجام شد. کد تایید حساب کاربری برای شما پیامک شد.')

        sms_text = SMS_TEXTS['verify_code'].format(code.code)
        send_sms(user.phone, sms_text)

        return user


class UserForm(forms.ModelForm):
    password = forms.CharField(label='رمز عبور', required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'phone', 'avatar',
                  'password', 'is_superuser', 'is_active', 'is_staff', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id:
            self.fields.pop('password')

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.pop('password', None)
        if password:
            user.set_password(password)
        user.is_active = True
        if commit:
            user.save()
        return user
