from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import *

class WalletSerializer(ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        queryset=User.objects.filter(block_status=False), write_only=True,
        validators=[UniqueValidator(queryset=Wallet.objects.all() , message='برای این کاربر قبلا کیف پول ثبت شده است')]
    )

    class Meta:
        model = Wallet
        fields = '__all__'
        depth = 1
