from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage

    readonly_fields = ['image_preview']

    def image_preview(self, place_image: PlaceImage):
        image = place_image.image

        return format_html(
            '<img src="{image_url}" style="max-height:200px;"/>',
            image_url=image.url,
            image_width=image.width
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'long_description')
        }),
        ('Координаты', {
            'fields': ('longitude', 'latitude')
        })
    )

    inlines = (
        PlaceImageInline,
    )
