from django.urls import path, include
from .views import *

urlpatterns = [
    path('dashboard/callprices/', CallPriceListView.as_view(), name='callprices-list'),
    path('dashboard/callprices/create/', CallPriceCreateView.as_view(), name='callprices-create'),
    path('dashboard/callprices/update/<int:pk>/', CallPriceUpdateView.as_view(), name='callprices-update'),
    path('dashboard/callprices/delete/<int:pk>/', CallPriceDeleteView.as_view(), name='callprices-delete'),

    path('callprices/create/', CallPriceCreateFrontView.as_view(), name='callprices-create-front'),
]
