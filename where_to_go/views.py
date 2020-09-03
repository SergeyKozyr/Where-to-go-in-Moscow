from django.shortcuts import render
from django.urls import reverse
from places.models import Place
from places.views import place as places_view


def index(request):

    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        places_geojson['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(places_view, args=[place.id])
                }
            }
        )

    context = {
        'places': places_geojson
    }
    return render(request, "index.html", context)
