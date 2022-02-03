from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название'
    )

    short_description = models.CharField(
        max_length=200,
        verbose_name='краткое описание'
    )
    long_description = models.TextField(
        verbose_name='полное описание'
    )

    longitude = models.FloatField(
        verbose_name='долгота'
    )
    latitude = models.FloatField(
        verbose_name='широта'
    )

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'
