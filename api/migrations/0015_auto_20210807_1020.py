# Generated by Django 3.2.6 on 2021-08-07 04:50

from django.db import migrations


def save_movie_order(apps, schema_editor):
    Movie = apps.get_model("api", "Movie")
    MovieOrderTemp = apps.get_model("api", "MovieOrderTemp")
    for movie in Movie.objects.all():
        MovieOrderTemp.objects.create(
            movie=movie, order=movie.order, package=movie.package
        )


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_auto_20210807_1013"),
    ]

    operations = [
        migrations.RunPython(save_movie_order),
    ]
