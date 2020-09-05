import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file')

    def handle(self, *args, **options):
        json_file = options['json_file']
        response = requests.get(json_file)
        response.raise_for_status()
        place_data = response.json()

        place, _ = Place.objects.get_or_create(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            longitude=place_data['coordinates']['lng'],
            latitude=place_data['coordinates']['lat']
        )

        images = place_data['imgs']
        for index, image_url in enumerate(images, 1):
            response = requests.get(image_url)
            response.raise_for_status()

            image = ContentFile(response.content)
            place_image = Image.objects.create(
                index=index,
                place=place,
            )
            place_image.image_file.save(f'{place.title} {index}.jpg', image, save=True)

        self.stdout.write(self.style.SUCCESS(f'{place.title} added!'))
