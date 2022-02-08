from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, reverse

from .models import Place


def get_place_geo_json(place: Place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [
                place.longitude,
                place.latitude
            ],
        },
        'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse(get_place_by_id, args=[place.id])
        }

    }


def index(request):
    places = Place.objects.all()

    places_geojson = {
        'type': 'FeatureCollection',
        'features': [
            get_place_geo_json(place) for place in places
        ]
    }

    return render(request, 'index.html', {'places': places_geojson})


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    return JsonResponse(
        {
            'title': place.title,
            'imgs': [
                place_image.image.url for place_image in place.images.all()
            ],
            'description_short': place.short_description,
            'description_long': place.long_description,
            'coordinates': {
                'lng': place.longitude,
                'lat': place.latitude
            }
        },
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )
