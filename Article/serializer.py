from django.conf import settings
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from Category.models import Category as Cat
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from Newsletter.models import Newsletter

User = get_user_model()

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        read_only_fields = [
            "created_at",
            "updated_at",
        ]

class ArticleSerializer(ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Cat.objects.filter(parent__isnull=False))
    image  = serializers.ImageField(required=False , use_url=True)
    class Meta:
        model = Article
        fields = '__all__'


    def update(self, instance, validated_data):
        if validated_data['status'] == 1:
            SendNewsLetterNotificationsEmails(validated_data, 'ویرایش')
        return super().update(instance , validated_data)


    def create(self, validated_data):
        if validated_data['status'] == 1:
            SendNewsLetterNotificationsEmails(validated_data , 'منتشر')
        return super().create(validated_data)


#################################################################################

def SendNewsLetterNotificationsEmails(blog , type):
    emails = Newsletter.objects.distinct().values_list('email', flat=True)
    for item in emails:
        msg = EmailMultiAlternatives('خبرنامه مقالات', 'خبرنامه مقالات', 'ashkan@gmail.com',
                                     [item])
        html_content = get_template('emails/newsletter/blog.html').render(
            {'email': item, 'blog': blog , 'type' : type , 'website_url' : settings.WEBSITE_URL})
        msg.attach_alternative(html_content, "text/html")
        msg.send()