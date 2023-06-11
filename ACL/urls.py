from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/roles/', RolesListView.as_view(), name='roles-list'),
    path('dashboard/roles/create/', RolesCreateView.as_view(), name='roles-create'),
    path('dashboard/roles/update/<int:pk>/', RolesUpdateView.as_view(), name='roles-update'),
    path('dashboard/roles/delete/<int:pk>/', RolesDeleteView.as_view(), name='roles-delete'),

    path('dashboard/permissions/', PermissionsListView.as_view(), name='permissions-list'),
    path('dashboard/permissions/create/', PermissionsCreateView.as_view(), name='permissions-create'),
    path('dashboard/permissions/update/<int:pk>/', PermissionsUpdateView.as_view(), name='permissions-update'),
    path('dashboard/permissions/delete/<int:pk>/', PermissionsDeleteView.as_view(), name='permissions-delete'),

    path('dashboard/role/user/', RoleUserListView.as_view(), name='role-user-list'),
    path('dashboard/role/user/create/', RoleUserCreateView.as_view(), name='role-user-create'),
    path('dashboard/role/user/update/<int:pk>/', RoleUserUpdateView.as_view(), name='role-user-update'),
    path('dashboard/role/user/delete/<int:pk>/', RoleUserDeleteView.as_view(), name='role-user-delete'),
]

urlpatterns += dashboard_urls
