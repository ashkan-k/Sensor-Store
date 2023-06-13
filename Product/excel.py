import xlrd
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import transaction
from django.utils.text import slugify
from unidecode import unidecode
from Product.models import Product, Color, Size


class Reader:
    override_values = False
    ignore_errors = False

    def __init__(self, **kwargs):
        self.ignore_errors = kwargs.get('ignore_errors', False)
        self.override_values = kwargs.get('override_values', False)

    @staticmethod
    def fetch_row_field(row_fields, i):
        try:
            return str(row_fields[i]).split('.')[0]
        except Exception as e:
            return ''

    def read(self, file_content):
        result = {
            'msg': '',
            'data': [],
            'products': [],
            'errors': [],
            'status': True
        }

        xlrd.xlsx.ensure_elementtree_imported(False, None)
        xlrd.xlsx.Element_has_iter = True

        try:
            workbook = xlrd.open_workbook(file_contents=file_content)
        except:
            result['msg'] = "خطا در خواند فایل اکسل. لطفا فایل را مجدد با فایل نمونه تطبیق دهید."
            result['status'] = False
            return result
        sheet = workbook.sheet_by_index(0)

        try:
            for index, row in enumerate(range(1, sheet.nrows)):
                row_error = ''
                try:
                    row_fields = sheet.row_values(row)

                    # required fields
                    title = self.fetch_row_field(row_fields, 0)
                    if not title:
                        row_error = 'نام محصول اجباری است.'

                    text = self.fetch_row_field(row_fields, 1)
                    if not text:
                        row_error = 'توضیحات اجباری است.'

                    price = self.fetch_row_field(row_fields, 2)
                    if not price:
                        row_error = 'قیمت محصول اجباری است.'

                    user_id = self.fetch_row_field(row_fields, 3)
                    if not user_id:
                        row_error = 'فروشنده محصول اجباری است.'

                    category_id = self.fetch_row_field(row_fields, 4)
                    if not category_id:
                        row_error = 'فروشنده محصول اجباری است.'

                    tags = self.fetch_row_field(row_fields, 5)
                    count = self.fetch_row_field(row_fields, 6)
                    suggestion_count = self.fetch_row_field(row_fields, 7)
                    status = self.fetch_row_field(row_fields, 8)
                    if status not in ['1', '0']:
                        row_error = 'وضعیت تایید محصول باید یکی از دو گزینه 0(غیر فعال)، 1(فعال) باشد.'

                    colors = []
                    colors_id = self.fetch_row_field(row_fields, 9)
                    if colors_id:
                        colors_id = colors_id.split(',')
                        try:
                            for item in colors_id:
                                item = int(item)
                                new_color = Color.objects.filter(id=item).first()
                                if not new_color:
                                    row_error = 'رنگی با این کد یافت نشد.'
                                else:
                                    colors.append(new_color)
                        except:
                            row_error = 'کد رنگ به فرمت درست نیست.'

                    sizes = []
                    sizes_id = self.fetch_row_field(row_fields, 10)
                    if sizes_id:
                        sizes_id = sizes_id.split(',')
                        try:
                            for item in sizes_id:
                                item = int(item)
                                new_size = Size.objects.filter(id=item).first()
                                if not new_size:
                                    row_error = 'سایزی با این کد یافت نشد.'
                                else:
                                    sizes.append(new_size)
                        except:
                            row_error = 'کد سایز به فرمت درست نیست.'


                except Exception as e:
                    row_error = 'خطا در اطلاعات'

                if row_error:
                    result['errors'].append([index + 2, row_error])
                    continue

                try:
                    result['data'].append({
                        'product_data': {
                            'title': title,
                            'text': text,
                            'price': price,
                            'user_id': user_id,
                            'category_id': category_id,
                            'tags': tags,
                            'count': count,
                            'suggestion_count': suggestion_count,
                            'status': status,
                        },
                        'colors': colors,
                        'sizes': sizes,
                    })
                except:
                    # Try except i guess is not needed, just added for being more sure
                    pass

        except Exception as e:
            result['msg'] = 'متاسفانه در فرمت فایل خطایی یافت شد. ' \
                            'لطفا محتوای فایل را با فرمت فایل نمونه مقایسه کنید.'
            result['status'] = False

        if len(result['errors']) > 0 and not self.ignore_errors:
            result['status'] = False
            return result

        # Now keep adding to database
        with transaction.atomic():
            for index in range(len(result['data'])):
                try:
                    row_error = ''
                    item = result['data'][index]
                    product_data = item.get('product_data')

                    slug = slugify(product_data.get('title'), True)

                    colors = item.pop('colors')
                    sizes = item.pop('sizes')

                    qs = Product.objects.filter(slug=slug)
                    if qs.count() > 0:
                        product = qs.first()
                        if product:
                            if not self.override_values:
                                # در این حالت نباید مقادیر کاربر به روز رسانی شوند.
                                continue
                            for key, value in product_data.items():
                                if not value:
                                    # فقط متغیرهایی که مقدار داشته باشند به روز رسانی می‌شوند.
                                    continue
                                setattr(product, key, value)

                            product.save()
                            result['users'].append([product, 'اطلاعات محصول به روز رسانی شد.'])
                    else:
                        product = Product.objects.create(**product_data)
                        result['products'].append([product, 'محصول ایجاد شد.'])

                    if colors:
                        product.colors.set(colors)
                    if sizes:
                        product.sizes.set(sizes)

                    product.save()

                    if row_error:
                        result['status'] = False
                        result['errors'].append([index + 2, row_error])
                except Exception as e:
                    result['status'] = False
                    result['errors'].append([index + 2, str(e)])

        if not self.ignore_errors:
            result['status'] = True
        return result
