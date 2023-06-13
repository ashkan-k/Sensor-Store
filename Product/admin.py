from django.contrib import admin
from .models import *
from django.utils.html import format_html

admin.site.register(Product)


@admin.register(NotifyUser)
class NotifyUserAdmin(admin.ModelAdmin):
    list_display = [ 'user' , 'product' , 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Image)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = [ "product" , "image" ]
    readonly_fields = ['created_at', 'updated_at']


    def image_tag(self, obj):
        if obj.image:
            img = obj.image.url
            return format_html('<img src="{}" width=50 />'.format(img))

        return None

    image_tag.short_description = 'عکس'



####################################################################################
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = [ 'name' , 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = [ 'title' , 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Suggest)
class SuggestAdmin(admin.ModelAdmin):
    list_display = [ 'product' , 'user' , 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']