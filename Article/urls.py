from django.urls import path, include
from .views import *

urlpatterns = [
    path('dashboard/articles/', ArticleListView.as_view(), name='articles-list'),
    path('dashboard/articles/create/', ArticleCreateView.as_view(), name='articles-create'),
    path('dashboard/articles/update/<int:pk>/', ArticleUpdateView.as_view(), name='articles-update'),
    path('dashboard/articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='articles-delete'),
]
