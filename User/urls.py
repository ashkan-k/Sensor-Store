from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/users/', UsersListView.as_view(), name='users-list'),
    path('dashboard/users/create/', UsersCreateView.as_view(), name='users-create'),
    path('dashboard/users/update/<int:pk>/', UsersUpdateView.as_view(), name='users-update'),
    path('dashboard/users/delete/<int:pk>/', UsersDeleteView.as_view(), name='users-delete'),
    path('dashboard/users/change/password/<int:pk>/', UserChangePasswordView.as_view(), name='users-change-password'),

    path('dashboard/profile/', ProfileView.as_view(), name='profile'),
    path('dashboard/change/password/', ChangePasswordView.as_view(), name='change-password'),
    path('dashboard/change/avatar/', ChangeAvatarView.as_view(), name='change-avatar'),

    # path('dashboard/users/export/excel/', UsersExportExcelView.as_view(), name='users-export-excel'),
]

urlpatterns += dashboard_urls
