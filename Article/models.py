from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from Article.helpers import ARTICLE_STATUS, ArticleStatusStatusArticle
from Category.models import Category
import time
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from Comment.models import Comment
from Like_And_DisLike.models import Like_And_DisLike
from utils.models import CustomModel


def upload_image(instance, filename):
    path = 'articles/' + slugify(instance.title, allow_unicode=True)
    name = str(time.time()) + '-' + str(get_random_string()) + '-' + filename

    return path + '/' + name


class Article(CustomModel):
    title = models.CharField(verbose_name='عنوان', max_length=50)
    slug = models.CharField(verbose_name='اسلاگ (نامک)', unique=True, blank=True, max_length=50)
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(verbose_name='عکس', upload_to=upload_image, null=True)
    status = models.CharField(verbose_name='وضعیت', default='draft', choices=ARTICLE_STATUS.CHOICES, max_length=50)
    viewCount = models.IntegerField(verbose_name='تعداد بازدید ها', default=0)

    author = models.ForeignKey(verbose_name='نویسنده', related_name='author_id', to=get_user_model(),
                               on_delete=models.CASCADE)
    # category = models.ForeignKey(verbose_name='دسته بندی', related_name='category_id', to=Category,
    #                              on_delete=models.CASCADE)

    comments = GenericRelation(Comment, related_query_name='articles')
    likes_and_dislikes = GenericRelation(Like_And_DisLike, related_query_name='articles')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    @property
    def get_status(self):
        return dict(ARTICLE_STATUS.CHOICES).get(self.status, '')

    @property
    def get_status_class(self):
        return dict(ArticleStatusStatusArticle.CHOICES).get(self.status, '')

    @property
    def get_image(self):
        return self.image.url if self.image else '---'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, True)
        return super().save(*args, **kwargs)
