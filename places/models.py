from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    index = models.PositiveSmallIntegerField('Позиция', default=0, blank=False, null=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место на карте')
    image_file = models.ImageField('Фотография')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['index']

    def __str__(self):
        return f'{self.index} {self.place}'
