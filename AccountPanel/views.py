from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from Permission.admin import IsSupporter
from Order.models import Order
from Order.serializer import OrderSerializer
from Wallet.models import Wallet
from WishList.models import Wishlist
from Product.models import NotifyUser
from Star.models import Star
from Comment.models import Comment
from Coupon.models import Coupon
from Coupon.serializer import CouponSerializer
from Comment.serializer import CommentSerializer
from Star.serializer import StarSerializer
from Product.serializer import NotifyUserSerializer
from WishList.serializer import WishlistSerializer
from config.pagination import CustomPagination
from rest_framework.viewsets import ModelViewSet
from .serializer import CartPanelSerializer, TicketPanelSerializer, WalletPanelSerializer
from Cart.models import Cart
from Ticket.models import Ticket , TicketAnswer , TicketQuestion
from Ticket.serializer import TicketQuestionSerializer , TicketAnswerSerializer
from rest_framework.generics import ListCreateAPIView


class SuccessOrdersViewSet(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    search_fields = [
        'user__username',
        'product__title',
        'product__price',
        'size__title',
        'color__name',
        'payment__ref_code',
        'name',
        'family',
        'email',
        'phone',
        'address1',
        'address2',
        'post_code',
    ]

    def get_queryset(self):
        return Order.objects.filter(status='sending', user=self.request.user)


class FailOrdersViewSet(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    search_fields = [
        'user__username',
        'product__title',
        'product__price',
        'size__title',
        'color__name',
        'payment__ref_code',
        'name',
        'family',
        'email',
        'phone',
        'address1',
        'address2',
        'post_code',
    ]

    def get_queryset(self):
        return Order.objects.filter(status__in=['posted', 'delivered'], user=self.request.user)


class WishListsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WishlistSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'delete']
    search_fields = ['product__title']

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)


class NotifyUsersViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NotifyUserSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'delete', 'put']
    search_fields = [
        'product__title',
        'product__slug',
    ]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        return NotifyUser.objects.filter(user=self.request.user)


class CartsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartPanelSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'delete']
    search_fields = ['product__title']

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class StarsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StarSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'delete' , 'put']
    search_fields = ['score' , 'product__title']

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        return Star.objects.filter(user=self.request.user)


class CommentsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'delete' , 'put']
    search_fields = ['title', 'text', 'user__username']

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)


class CouponsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CouponSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'delete']
    search_fields = ['code', 'percent', 'expiration']

    def get_queryset(self):
        return Coupon.objects.filter(user=self.request.user)


class TicketsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketPanelSerializer
    pagination_class = CustomPagination
    http_method_names = ['get', 'delete' , 'put']
    search_fields = ['title']

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class AllUsersTicketsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated , IsSupporter]
    queryset = Ticket.objects.all()
    serializer_class = TicketPanelSerializer
    pagination_class = CustomPagination
    http_method_names = ['get']
    search_fields = ['title']


class TicketQuestionsViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketQuestionSerializer
    pagination_class = CustomPagination

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def get_queryset(self):
        return TicketQuestion.objects.filter(ticket__user=self.request.user)


class TicketAnswersViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticated , IsSupporter]
    queryset = TicketAnswer.objects.all()
    serializer_class = TicketAnswerSerializer
    pagination_class = CustomPagination

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)



class WalletView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WalletPanelSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return Wallet.objects.filter(status=True , user=self.request.user)