from django.urls import path, include
from .views import *

urlpatterns = [
    path('dashboard/coupons/', CouponListView.as_view(), name='coupons-list'),
    path('dashboard/coupons/create/', CouponCreateView.as_view(), name='coupons-create'),
    path('dashboard/coupons/update/<int:pk>/', CouponUpdateView.as_view(), name='coupons-update'),
    path('dashboard/coupons/delete/<int:pk>/', CouponDeleteView.as_view(), name='coupons-delete'),
]
