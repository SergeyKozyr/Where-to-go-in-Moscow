from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['thumbnail', ]
    fields = ('image_file', 'thumbnail', 'index')

    def thumbnail(self, instance):
        return format_html('<img src={} height={} />', instance.image_file.url, 200)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
