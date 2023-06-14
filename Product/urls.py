from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('dashboard/products/', ProductListView.as_view(), name='products-list'),
    path('dashboard/products/create/', ProductCreateView.as_view(), name='products-create'),
    path('dashboard/products/update/<int:pk>/', ProductUpdateView.as_view(), name='products-update'),
    path('dashboard/products/delete/<int:pk>/', ProductDeleteView.as_view(), name='products-delete'),

    path('dashboard/colors/', ColorListView.as_view(), name='colors-list'),
    path('dashboard/colors/create/', ColorCreateView.as_view(), name='colors-create'),
    path('dashboard/colors/update/<int:pk>/', ColorUpdateView.as_view(), name='colors-update'),
    path('dashboard/colors/delete/<int:pk>/', ColorDeleteView.as_view(), name='colors-delete'),

    path('dashboard/sizes/', SizeListView.as_view(), name='sizes-list'),
    path('dashboard/sizes/create/', SizeCreateView.as_view(), name='sizes-create'),
    path('dashboard/sizes/update/<int:pk>/', SizeUpdateView.as_view(), name='sizes-update'),
    path('dashboard/sizes/delete/<int:pk>/', SizeDeleteView.as_view(), name='sizes-delete'),

    path("dashboard/products/import/", ProductImportView.as_view(), name='products-import'),

]

# router = SimpleRouter()
# router.register('accepted' , ProductAcceptedViewsSet)
# router.register('rejected' , ProductRejectedViewsSet)
# router.register('notify_users/active' , ActiveNotifyUsersViewsSet)
# router.register('notify_users/inactive' , InActiveNotifyUsersViewsSet)
# router.register('images' , ImagesViewSet)
# router.register('colors' , ColorsViewSet)
# router.register('sizes' , SizesViewSet)
# router.register('suggests' , SuggestsViewSet)

# urlpatterns = [
#     path('' , include(router.urls)),
#     path('WithOutPagination/' , ProductAllList.as_view()),
#     path('images/create/multiple/' , ProductImagesView.as_view()),
#     path('users/list/' , UsersListView.as_view()),
#     path('change/accepted' , ProductChangeAccepted.as_view()),
#     path('notify_users/change/active/', NotifyUserChangeActive.as_view()),

#     path('colors/all/WithOutPagination/' , ColorListWithOutPaginationView.as_view()),
#     path('sizes/all/WithOutPagination/', SizeListWithOutPaginationView.as_view()),
# ]
