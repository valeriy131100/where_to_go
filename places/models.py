from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название'
    )

    short_description = models.TextField(
        verbose_name='краткое описание'
    )
    long_description = HTMLField(
        verbose_name='полное описание'
    )

    longitude = models.FloatField(
        verbose_name='долгота'
    )
    latitude = models.FloatField(
        verbose_name='широта'
    )

    def __str__(self):
        return f'Место "{self.title}"'

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        verbose_name='изображение'
    )
    position = models.IntegerField(
        default=0,
        verbose_name='позиция'
    )

    def __str__(self):
        return f'Изображение места "{self.place.title}"'

    class Meta:
        verbose_name = 'изображение места'
        verbose_name_plural = 'изображения мест'
        ordering = ['position']
