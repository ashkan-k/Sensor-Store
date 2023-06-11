from re import sub
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
User = get_user_model()

class CheckEmailVerification:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            token = sub('Bearer ', '', request.META.get('HTTP_AUTHORIZATION', None))
            user_id = AccessToken(token).payload['user_id']
            user = User.objects.get(pk=user_id)
        except:
            user = request.user

        if request.path.startswith('/api/panel/') and user.is_authenticated and not user.email_verified_at:
            raise PermissionDenied('شما باید ابتدا ایمیل خود را تایید و احراز هویت را کامل کنید')

        response = self.get_response(request)
        return response