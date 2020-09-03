from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    placeId = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    index = models.SmallIntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image_file = models.ImageField()

    def __str__(self):
        return f'{self.index} {self.place}'
