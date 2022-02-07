from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Загружает место из json-файла в Интернете'

    def add_arguments(self, parser):
        parser.add_argument('place_urls', nargs='+')

    def handle(self, place_urls, *args, **kwargs):
        for place_url in place_urls:
            response = requests.get(place_url)
            response.raise_for_status()

            place_description = response.json()

            coordinates = place_description['coordinates']
            title = place_description['title']
            short_description = place_description['description_short']
            long_description = place_description['description_long']

            place, created = Place.objects.get_or_create(
                longitude=float(coordinates['lng']),
                latitude=float(coordinates['lat']),
                defaults={
                    'title': title,
                    'short_description': short_description,
                    'long_description': long_description
                }
            )

            if not created:
                continue

            for image_url in place_description['imgs']:
                image_name = urlparse(image_url).path.split('/')[-1]
                image_response = requests.get(image_url)
                image_response.raise_for_status()

                place_image = PlaceImage(place=place)
                place_image.image.save(
                    image_name,
                    ContentFile(image_response.content),
                    save=True
                )





