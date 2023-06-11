from django.core.exceptions import ValidationError

def check_user_exist(user, new_phone):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    exists_user = User.objects.filter(phone=new_phone).first()
    if exists_user and exists_user.phone != user.phone:
        raise ValidationError([
            ValidationError('کاربری با این موبایل قبلا ثبت شده است!', code='duplicate'),
        ])


MARITAL_STATUS_CHOICES = (
    ('S', 'مجرد'),
    ('M', 'متاهل'),
)

EDUCATION_LEVEL_CHOICES = (
    ('S', 'ابتدایی'),
    ('FH', 'متوسطه اول'),
    ('SH', 'متوسطه دوم'),
    ('AD', 'کاردانی'),
    ('M', 'کارشناسی'),
    ('O', 'سایر'),
)

class INTRO_METHOD:
    WEBSITE = "website"
    ADS = "ads"
    SOCIAL = "social"
    SMS_ADS = "sms_ads"
    STUDENTS_AND_TEACHERS = "students_and_teachers"
    CHOICES = (
        (WEBSITE, "از طریق سایت"),
        (ADS, "تبلیغات تراکتی"),
        (SOCIAL, "اپلیکیشن های مجازی"),
        (SMS_ADS, "پیامک تبلیغاتی"),
        (STUDENTS_AND_TEACHERS, "دانش اموزان و همکاران"),
    )