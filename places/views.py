from django.shortcuts import render

from .models import Place


def serialize_place(place: Place):
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
            # replace this
            'detailsUrl': './static/places/moscow_legends.json'
        }

    }


def index(request):
    places = Place.objects.prefetch_related('images')

    places_context = {
        'type': 'FeatureCollection',
        'features': [
            serialize_place(place) for place in places
        ]
    }

    return render(request, 'index.html', {'places': places_context})
