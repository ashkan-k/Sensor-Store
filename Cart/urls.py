from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/carts/', CartListView.as_view(), name='carts-list'),
    path('dashboard/carts/delete/<int:pk>/', CartDeleteView.as_view(), name='carts-delete'),
]

front_urls = [
    path('carts/add/', CartView.as_view(), name='carts-add'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls
