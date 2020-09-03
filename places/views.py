# from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place, Image


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = Image.objects.filter(place=place)
    place_details = {

        'title': place.title,
        'imgs': [img.image_file.url for img in place_images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {'lat': place.latitude, 'lng': place.longitude}
    }
    return JsonResponse(place_details, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
