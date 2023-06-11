from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify/', VerifyCodeView.as_view(), name='verify-code'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout'),

    path('password/reset/', ResetPasswordView.as_view(), name='password-reset'),
    path('password/reset/confirm/', VerifyCodeView.as_view(), name='password-reset-confirm'),
    path('password/reset/enter/', ResetPasswordEnterView.as_view(), name='password-reset-enter'),
]
