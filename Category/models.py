from django.db import models
from django.utils.text import slugify
from utils.models import CustomModel
from utils.validator import validate_file_size


def upload_image(instance, filename):
    path = 'categories/' + slugify(f"{instance.name}", allow_unicode=True)
    return path + '/' + filename


###################################################################################


class Category(CustomModel):
    name = models.CharField(verbose_name='نام', max_length=50)
    slug = models.CharField(verbose_name='اسلاگ (نامک)', unique=True, blank=True, max_length=50)
    image = models.ImageField(
        null=True, blank=True,
        verbose_name='عکس', upload_to=upload_image,
        validators=[validate_file_size]
    )
    parent = models.ForeignKey(verbose_name='والد', to='Category', related_name='childs', on_delete=models.CASCADE,
                               null=True, blank=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, True)
        return super().save(*args, **kwargs)
