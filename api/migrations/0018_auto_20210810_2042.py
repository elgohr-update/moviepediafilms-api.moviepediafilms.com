# Generated by Django 3.2.6 on 2021-08-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_auto_20210807_1027"),
    ]

    operations = [
        migrations.AddField(
            model_name="package",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="movies",
            field=models.ManyToManyField(related_name="orders", to="api.Movie"),
        ),
        migrations.DeleteModel(
            name="MovieOrderTemp",
        ),
    ]
