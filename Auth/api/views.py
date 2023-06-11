from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from Auth.api.serializers import *
from django.contrib.auth import get_user_model

from Auth.helpers import create_code
from Auth.models import Code

User = get_user_model()


class UserAuthVS(GenericViewSet):
    @action(
        methods=["get", "post"],
        detail=False,
        url_path="code/send",
        serializer_class=CodeSerializer,
    )
    def code_send(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(True)
        serializer.save()
        phone = serializer.data['phone']
        user = User.objects.filter(phone=phone).first()

        if user:
            try:
                return Response({'message': 'پیامک حاوی کد تایید با موفقیت ارسال شد.', 'phone': user.phone}, 200)
            except:
                return Response(
                    {'error': 'خطایی هنگام ارسال پیامک حاوی کد یکبار مصرف پیش آمده است! لطفا دوباره امتحان کنید.'}, 400)

        return Response({'error': 'کاربری با این شماره موبایل وجود ندارد!'}, 404)
