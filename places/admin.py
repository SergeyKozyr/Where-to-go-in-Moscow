from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['thumbnail', ]
    fields = ('image_file', 'thumbnail', 'index')
    extra = 0

    def thumbnail(self, instance):
        if instance.image_file:
            return format_html('<img src={} height={} />', instance.image_file.url, 200)
        else:
            return 'Здесь будет превью, когда вы добавите файл'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [ImageInline]
