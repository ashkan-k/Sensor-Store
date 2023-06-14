from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/payments/', PaymentListView.as_view(), name='payments-list'),
    path('dashboard/payments/delete/<int:pk>/', PaymentDeleteView.as_view(), name='payments-delete'),
]

urlpatterns += dashboard_urls
