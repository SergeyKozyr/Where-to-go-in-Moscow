# Generated by Django 3.1 on 2020-09-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('placeId', models.CharField(max_length=255)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
        ),
    ]
