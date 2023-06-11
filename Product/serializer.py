from django.conf import settings
from rest_framework import serializers
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth import get_user_model
from Category.models import Category
from Newsletter.models import Newsletter

User = get_user_model()


########################################################################################################

def SendUserNotificationsEmail(product, id):
    emails = NotifyUser.objects.filter(product_id=id, active=True).distinct().values_list('user__email', flat=True)
    msg = EmailMultiAlternatives('اطلاع رسانی محصول', 'اطلاع رسانی محصول', 'ashkan@gmail.com',
                                 list(emails))
    html_content = get_template('emails/product_notification/product_notification.html').render(
        {'product': product , 'website_url' : settings.WEBSITE_URL})
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def SendNewsLetterNotificationsEmails(product, type):
    emails = Newsletter.objects.distinct().values_list('email', flat=True)
    for item in emails:
        msg = EmailMultiAlternatives('خبرنامه محصولات', 'خبرنامه محصولات', 'ashkan@gmail.com',
                                     [item])
        html_content = get_template('emails/newsletter/product.html').render(
            {'email': item, 'product': product, 'type': type , 'website_url' : settings.WEBSITE_URL})
        msg.attach_alternative(html_content, "text/html")
        msg.send()


############################################################################################################

class ImageSerializer(ModelSerializer):
    image = serializers.ImageField(required=False, use_url=True)

    class Meta:
        model = Image
        fields = '__all__'

    read_only_fields = [
        "created_at",
        "updated_at",
    ]


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

    read_only_fields = [
        "created_at",
        "updated_at",
    ]


class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

    read_only_fields = [
        "created_at",
        "updated_at",
    ]


class SuggestSerializer(ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        source='user',
        queryset=User.objects.filter(block_status=False), write_only=True
    )
    product_id = serializers.PrimaryKeyRelatedField(
        source='product',
        queryset=Product.objects.filter(status=True), write_only=True
    )

    class Meta:
        model = Suggest
        fields = '__all__'
        depth = 1

    read_only_fields = [
        "created_at",
        "updated_at",
    ]


class ProductSerializer(ModelSerializer):
    original_image = serializers.ImageField(required=False, use_url=True)
    images = ImageSerializer(many=True, read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    #################################
    color_id = serializers.PrimaryKeyRelatedField(
        many=True,
        source='colors',
        queryset=Color.objects.all(), write_only=True
    )

    size_id = serializers.PrimaryKeyRelatedField(
        many=True,
        source='sizes',
        queryset=Size.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    def update(self, instance, validated_data):
        if validated_data['status'] and validated_data['count'] > 0:
            SendUserNotificationsEmail(validated_data, instance.id)

        if validated_data['status'] and not validated_data['is_removed'] == 1:
            SendNewsLetterNotificationsEmails(validated_data, 'ویرایش')

        return super().update(instance, validated_data)


    def create(self, validated_data):
        if validated_data['status']:
            SendNewsLetterNotificationsEmails(validated_data, 'منتشر')
        return super().create(validated_data)


class NotifyUserSerializer(ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = NotifyUser
        fields = '__all__'
        depth = 1

        read_only_fields = [
            "created_at",
            "updated_at",
        ]
