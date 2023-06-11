from django.urls import path
from .views import *

urlpatterns = []

dashboard_urls = [
    path('dashboard/suggestions/', SuggestionListView.as_view(), name='suggestions-list'),
    path('dashboard/suggestions/create/', SuggestionCreateView.as_view(), name='suggestions-create'),
    path('dashboard/suggestions/update/<int:pk>/', SuggestionUpdateView.as_view(), name='suggestions-update'),
    path('dashboard/suggestions/delete/<int:pk>/', SuggestionDeleteView.as_view(), name='suggestions-delete'),

    path('dashboard/contact_us/', ContactUsListView.as_view(), name='contact_us-list'),
    path('dashboard/contact_us/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contact_us-delete'),
]

front_urls = [
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
]

urlpatterns += dashboard_urls
urlpatterns += front_urls
