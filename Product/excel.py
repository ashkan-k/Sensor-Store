import xlrd
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import transaction
from unidecode import unidecode
from Product.models import Product


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

        if not self.company:
            print('vvvvvvvvvvvvvvvvvvvvvvvvvv')
            result['msg'] = "لطفا شرکت را انتخاب کنید."
            result['status'] = False
            return result

        print(self.company)

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

                    # one of first_name or last_name is required
                    first_name = self.fetch_row_field(row_fields, 0)
                    last_name = self.fetch_row_field(row_fields, 1)
                    if not first_name and not last_name:
                        row_error = 'حداقل یکی از فیلدهای نام یا نام خانوادگی باید پر شده باشد.'

                    # mobile should be in correct format (Required field)
                    mobile = ''
                    try:
                        mobile = self.fetch_row_field(row_fields, 2)
                        mobile = self.validate_mobile(mobile) if mobile else ''
                    except:
                        row_error = "موبایل وارد شده معتبر نیست"

                    # Optional
                    national_id = ''
                    try:
                        national_id = self.fetch_row_field(row_fields, 3)
                        if national_id:
                            national_id = self.validate_national_id(self.fetch_row_field(row_fields, 3))
                    except:
                        row_error = "کد ملی وارد شده معتبر نیست"

                    # one of mobile or national_id should be provided.
                    if not username:
                        username = mobile
                    if not username:
                        username = national_id
                    if not username:
                        row_error = 'حداقل یکی از فیلدهای نام کاربری، موبایل یا کد ملی باید وجود داشته باشد.'

                    # Get email
                    email = ''
                    try:
                        e = row_fields[4]
                        if e:
                            email = self.validate_email(e)
                    except:
                        row_error = 'ایمیل وارد شده معتبر نیست.'

                    # Other info
                    gender = self.fetch_row_field(row_fields, 5)
                    if gender:
                        gender = 'F' if str(gender).upper() == 'F' else 'M'
                    birth_date = self.fetch_row_field(row_fields, 6)
                    if birth_date:
                        birth_date = str(birth_date).replace('-', '/')
                        birth_date = unidecode(birth_date)
                        birth_date = string_to_jdatetime(birth_date, only_date=True)
                        if not birth_date:
                            row_error = 'تاریخ تولد به فرمت مناسب ارسال نشده است. به طور مثال 1399/03/01'
                    if not birth_date:
                        birth_date = None

                    # personnel_code = self.fetch_row_field(row_fields, 8)
                    # address = self.fetch_row_field(row_fields, 9)
                    # father_name = self.fetch_row_field(row_fields, 10)
                    # identity_number = self.fetch_row_field(row_fields, 11)
                    # work_place = self.fetch_row_field(row_fields, 12)
                    # work_position = self.fetch_row_field(row_fields, 13)
                    password = self.validate_password(self.fetch_row_field(row_fields, 7))

                    # Get group to assign to user (optional)
                    group = []
                    group_id = self.fetch_row_field(row_fields, 8)
                    if group_id:
                        group_id = group_id.split(',')
                        try:
                            for item in group_id:
                                item = int(item)
                                new_group = Group.objects.filter(id=item).first()
                                if not new_group:
                                    row_error = 'گروهی با این کد یافت نشد.'
                                else:
                                    group.append(new_group)
                        except:
                            row_error = 'کد گروه به فرمت درست نیست.'

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
