from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/settings/', SettingsList.as_view(), name='settings-list'),
    path('dashboard/settings/create/', SettingsCreate.as_view(), name='settings-create'),
    path('dashboard/settings/update/<int:pk>/', SettingsUpdate.as_view(), name='settings-update'),
    path('dashboard/settings/delete/<int:pk>/', SettingsDelete.as_view(), name='settings-delete'),
]
