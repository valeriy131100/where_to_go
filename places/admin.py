from django.contrib import admin

from .models import Place, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


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


admin.site.register(Place, PlaceAdmin)
