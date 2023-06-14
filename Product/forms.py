from django import forms
from django.forms import ClearableFileInput

from Product.models import Product, Color, Size, Gallery


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'likes_and_dislikes']


class ExcelImportForm(forms.Form):
    file = forms.FileField(
        required=True,
        label="فایل ‌اکسل",
        widget=forms.FileInput(attrs={"accept": ".xls,.xlsx"}),
        help_text="فرمت فایل ورودی باید xls. یا xlsx. باشد",
    )
    ignore_errors = forms.BooleanField(
        required=False,
        label='خطاهای موجود در فایل در نظر گرفته نشوند؟',
        help_text='با انتخاب این گزینه در صورتی که در هر کدام از سطرهای فایل اکسل خطایی وجود داشته باشد،'
                  ' از آن صرف نظر شده و سطرهایی که اطلاعات آن‌ها صحیح است قرار داده می‌شوند.'
                  ' در غیر این صورت هیچ کدام از اطلاعات وارد نمی‌شود.'
    )
    override_values = forms.BooleanField(
        required=False,
        label='اطلاعات کاربران به روز رسانی شود؟',
        help_text='با انتخاب این گزینه، در صورتی که سطری از کاربرها قبلا تعریف شده باشد،'
                  ' و مجدد در فایل اکسل وجود داشته باشد، اطلاعات کاربر به روز رسانی خواهند شد.'
    )


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
        widgets = {
            "resumes": ClearableFileInput(attrs={"multiple": True}),
        }
