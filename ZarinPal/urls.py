from django.urls import path
from .views import *

urlpatterns = [
    path('request/', pay , name='request-payment'),
    path('verify/', verify , name='verify'),

    path('panel/wallet/charge/', charge , name='wallet-charge'),
    path('panel/wallet/charge/verify/', charge_verify, name='wallet-charge-verify'),
]