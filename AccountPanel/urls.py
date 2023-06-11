from django.urls import path , include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('wishlists' , WishListsViewsSet , basename='panel-wishlist')
router.register('notify_users' , NotifyUsersViewsSet , basename='panel-notifies')
router.register('carts' , CartsViewsSet , basename='panel-carts')
router.register('stars' , StarsViewsSet , basename='panel-stars')
router.register('comments' , CommentsViewsSet , basename='panel-comments')
router.register('coupons' , CouponsViewsSet , basename='panel-coupons')

ticket_router = SimpleRouter()
ticket_router.register('list' , TicketsViewsSet , basename='panel-tickets-list')
ticket_router.register('all_users' , AllUsersTicketsViewsSet , basename='panel-tickets-all_users')
ticket_router.register('questions' , TicketQuestionsViewsSet , basename='panel-tickets-questions')
ticket_router.register('answers' , TicketAnswersViewsSet , basename='panel-tickets-answers')


urlpatterns = [
    path('', include(router.urls)),
    path('tickets/', include(ticket_router.urls)),
    path('orders/success/' , SuccessOrdersViewSet.as_view()),
    path('orders/fail/', FailOrdersViewSet.as_view()),

    path('wallet/' , WalletView.as_view())
]