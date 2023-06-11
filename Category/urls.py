from django.urls import path, include
from .views import *

urlpatterns = [
    path('dashboard/categories/', CategoryListView.as_view(), name='categories-list'),
    path('dashboard/categories/create/', CategoryCreateView.as_view(), name='categories-create'),
    path('dashboard/categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='categories-update'),
    path('dashboard/categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='categories-delete'),
]
