from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from Permission.admin import IsAdminMixin
from config.pagination import CustomPagination
from .models import *
from .serializer import *

class WalletsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminMixin]
    queryset = Wallet.objects.filter(status=True)
    serializer_class = WalletSerializer
    pagination_class = CustomPagination
    search_fields = ['user__username' , 'amount']