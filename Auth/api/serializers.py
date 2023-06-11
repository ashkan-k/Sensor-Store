from django.core.validators import RegexValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from Auth.helpers import create_code
from Auth.models import Code
from Sms.helpers import send_sms
from Sms.sms_texts import SMS_TEXTS
from utils.validator import mobile_regex

User = get_user_model()


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6, required=False, validators=[RegexValidator(
        regex=r'^-?\d+\Z',
        message="کد تایید باید عددی باشد",
    )])
    phone = serializers.CharField(max_length=11, min_length=11, required=True, validators=[mobile_regex])

    def save(self, **kwargs):
        phone = self.validated_data.get('phone')
        user = User.objects.filter(phone=phone).first()
        if not user:
            raise serializers.ValidationError('کاربری با این شماره موبایل وجود ندارد!', code='phone')

        code = Code.objects.create_new_code(user)
        sms_text = SMS_TEXTS['verify_code'].format(code.code)
        send_sms(user.phone, sms_text)
        return code


class CodeConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6, required=True, validators=[RegexValidator(
        regex=r'^-?\d+\Z',
        message="کد تایید باید عددی باشد",
    )])
    phone = serializers.CharField(max_length=11, min_length=11, required=True, validators=[mobile_regex])

    def save(self, **kwargs):
        phone = self.validated_data.get('phone')
        code = create_code()

        user = User.objects.filter(phone=phone).first()
        if not user:
            raise serializers.ValidationError('کاربری با این شماره موبایل وجود ندارد!', code='phone')


        code = Code.objects.create(code=code, user=user)
        # TODO send code with sms
        return code
