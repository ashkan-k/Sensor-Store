from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Product.models import Product
from Cart.models import Cart
from django.contrib.auth import get_user_model

from Ticket.models import TicketQuestion, TicketAnswer, Ticket
from Wallet.models import Wallet

User = get_user_model()

class CartPanelSerializer(ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        queryset=User.objects.filter(block_status=False), write_only=True
    )
    product_id = serializers.PrimaryKeyRelatedField(
        source='product',
        queryset=Product.objects.filter(status=True), write_only=True
    )

    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1

    read_only_fields = '__all__'



class TicketPanelSerializer(ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    answers_count = serializers.SerializerMethodField()

    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        queryset=User.objects.filter(block_status=False), write_only=True
    )

    def get_questions_count(self, ticket):
        count = TicketQuestion.objects.filter(ticket=ticket).count()
        return count

    def get_answers_count(self, ticket):
        count = TicketAnswer.objects.filter(ticket=ticket).count()
        return count

    class Meta:
        model = Ticket
        fields = [
            'id',
            'title',
            'status',
            'user_id',
            'user',
            'questions',
            'answers',
            'questions_count',
            'answers_count',
            'created_at',
            'updated_at',
        ]
        depth = 1



class WalletPanelSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)
    class Meta:
        fields = ['amount']


    def create(self, validated_data):
        user = self.context.get('request', None).user
        wallet = Wallet.objects.filter(status=True , user=user).first()

        if wallet:
            wallet.amount += validated_data['amount']
            wallet.save()

        return wallet