from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.TextField()
    description_long = HTMLField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    index = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image_file = models.ImageField()

    class Meta:
        ordering = ['index']

    def __str__(self):
        return f'{self.index} {self.place}'
