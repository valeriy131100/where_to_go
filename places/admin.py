from django.contrib import admin

from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'long_description')
        }),
        ('Координаты', {
            'fields': ('longitude', 'latitude')
        })
    )


admin.site.register(Place, PlaceAdmin)
