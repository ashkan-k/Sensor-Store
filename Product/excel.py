import xlrd
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import transaction
from unidecode import unidecode
from Product.models import Product, Color


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
                    username = self.fetch_row_field(row_fields, 10000)  # Optional

                    # required fields
                    title = self.fetch_row_field(row_fields, 0)
                    if not title:
                        row_error = 'نام محصول اجباری است.'

                    text = self.fetch_row_field(row_fields, 1)
                    if not text:
                        row_error = 'توضیحات اجباری است.'

                    price = self.fetch_row_field(row_fields, 3)
                    if not price:
                        row_error = 'قیمت محصول اجباری است.'

                    user_id = self.fetch_row_field(row_fields, 4)
                    if not user_id:
                        row_error = 'فروشنده محصول اجباری است.'

                    category_id = self.fetch_row_field(row_fields, 5)
                    if not category_id:
                        row_error = 'فروشنده محصول اجباری است.'

                    tags = self.fetch_row_field(row_fields, 6)
                    price = self.fetch_row_field(row_fields, 7)
                    count = self.fetch_row_field(row_fields, 8)
                    suggestion_count = self.fetch_row_field(row_fields, 9)
                    status = self.fetch_row_field(row_fields, 10)
                    if status not in [1, 0]:
                        row_error = 'وضعیت تایید محصول باید یکی از دو گزینه 0(غیر فعال)، 1(فعال) باشد.'

                    colors = []
                    colors_id = self.fetch_row_field(row_fields, 11)
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
                    sizes_id = self.fetch_row_field(row_fields, 11)
                    if sizes_id:
                        sizes_id = sizes_id.split(',')
                        try:
                            for item in sizes_id:
                                item = int(item)
                                new_size = Color.objects.filter(id=item).first()
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
                        'user': {
                            'username': username,
                            'first_name': first_name,
                            'last_name': last_name,
                            'email': email,
                            'mobile': mobile,
                            'password': password,
                            'national_id': national_id,
                            # 'personnel_code': personnel_code,
                            'birth_date': birth_date,
                            # 'address': address,
                            # 'type': user_type,
                            'gender': gender,
                            # 'father_name': father_name,
                            # 'work_place': work_place,
                            # 'work_position': work_position,
                            # 'identity_number': identity_number,
                        },
                        'group': group,
                        # 'company': company,
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
                    user_data = item.get('user')

                    username = user_data.pop('username')
                    mobile = user_data.pop('mobile')
                    national_id = user_data.pop('national_id')
                    # identity_number = user_data.pop('identity_number')
                    # father_name = user_data.pop('father_name')

                    # work_place = user_data.pop('work_place')
                    # work_position = user_data.pop('work_position')
                    # personnel_code = user_data.pop('personnel_code')
                    # company = item.pop('company')
                    group = item.pop('group')

                    if username:
                        qs = User.objects.filter(username=username)
                    if mobile and not qs:
                        qs = User.objects.filter(mobile=mobile)
                    # if national_id and not qs:
                    #     qs = User.objects.filter(national_id=national_id)

                    count = qs.count()
                    if count > 1:
                        row_error = '{} کاربر دیگر با این شماره موبایل یا کد ملی قبلا تعریف شده است.'.format(count - 1)
                    else:
                        user = qs.first()
                        if user:
                            if not self.override_values:
                                # در این حالت نباید مقادیر کاربر به روز رسانی شوند.
                                continue
                            for key, value in user_data.items():
                                if not value:
                                    # فقط متغیرهایی که مقدار داشته باشند به روز رسانی می‌شوند.
                                    continue
                                if key == 'password':
                                    user.set_password(value)
                                else:
                                    setattr(user, key, value)
                            user.save()

                            if group:
                                user.add_groups(group)
                            result['products'].append([user, 'اطلاعات کاربر به روز رسانی شد.'])
                        else:
                            user = User.objects.create_user(
                                mobile=mobile,
                                username=username,
                                national_id=national_id,
                                # father_name=father_name,
                                # identity_number=identity_number,
                                **user_data
                            )

                            result['products'].append([user, 'کاربر ایجاد شد.'])

                        # if personnel_code:
                        #     user.profile.personnel_code = personnel_code
                        # if work_position:
                        #     user.profile.work_position = work_position
                        # if work_place:
                        #     user.profile.work_place = work_place
                        # user.profile.save()

                        if group:
                            user.add_groups(group)

                        if self.company:
                            user.set_company(self.company)
                            print('bbbbbbbbbbbbbbbbbbbbbbbbbb')
                            print(user.company)

                    if row_error:
                        result['status'] = False
                        result['errors'].append([index + 2, row_error])
                except Exception as e:
                    result['status'] = False
                    result['errors'].append([index + 2, str(e)])

        if not self.ignore_errors:
            result['status'] = True
        return result
