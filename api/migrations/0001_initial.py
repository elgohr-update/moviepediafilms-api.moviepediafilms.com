# Generated by Django 3.1.2 on 2020-10-03 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AwardType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Badge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("icon", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("S", "Submitted"),
                            ("R", "Rejected"),
                            ("P", "Published"),
                            ("H", "Hidden"),
                            ("A", "Archived"),
                        ],
                        max_length=1,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("link", models.URLField()),
                ("runtime", models.FloatField()),
                ("about", models.TextField()),
                ("poster", models.URLField(blank=True, null=True)),
                ("month", models.DateField(blank=True, null=True)),
                ("publish_on", models.DateTimeField(blank=True, null=True)),
                ("jury_rating", models.FloatField(blank=True, null=True)),
                ("audience_rating", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MovieFrame",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="MovieGenre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="MovieLanguage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Watchlist",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("movies", models.ManyToManyField(to="api.Movie")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("mobile", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Others")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("dob", models.DateField(blank=True, null=True)),
                ("image", models.URLField(blank=True, null=True)),
                ("mcoins", models.FloatField(default=0)),
                ("rank", models.IntegerField(default=-1)),
                ("score", models.FloatField(default=0)),
                ("level", models.IntegerField(default=1)),
                ("pop_score", models.FloatField(default=0)),
                ("badges", models.ManyToManyField(blank=True, to="api.Badge")),
                ("follows", models.ManyToManyField(blank=True, to="api.Profile")),
                ("roles", models.ManyToManyField(blank=True, to="api.Role")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.CharField(max_length=100, unique=True)),
                ("payment_id", models.CharField(max_length=100, null=True)),
                ("receipt_number", models.CharField(max_length=32)),
                ("amount", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MovieUserRating",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.FloatField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.movie"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MovieReview",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("published_at", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField()),
                ("liked_by", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="MoviePoster",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("link", models.URLField()),
                ("primary", models.BooleanField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.movie"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="movie",
            name="frames",
            field=models.ManyToManyField(blank=True, to="api.MovieFrame"),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="api.MovieGenre"),
        ),
        migrations.AddField(
            model_name="movie",
            name="lang",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.movielanguage"
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.order",
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="profiles",
            field=models.ManyToManyField(to="api.Profile"),
        ),
        migrations.CreateModel(
            name="Judge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=200)),
                ("about", models.TextField()),
                ("recom_movies", models.ManyToManyField(to="api.Movie")),
            ],
        ),
        migrations.CreateModel(
            name="GameAttempt",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("started_at", models.DateTimeField(auto_now_add=True)),
                ("ended_at", models.DateTimeField(auto_now_add=True)),
                ("score", models.FloatField(blank=True, null=True)),
                ("multiplier", models.FloatField()),
                (
                    "badge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.badge"
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.movie"
                    ),
                ),
                ("selected_frames", models.ManyToManyField(to="api.MovieFrame")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BadgeClaim",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("amount", models.FloatField()),
                (
                    "state",
                    models.CharField(
                        choices=[("C", "Created"), ("S", "Success"), ("F", "Failed")],
                        max_length=1,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Award",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("awarded_at", models.DateTimeField()),
                (
                    "movie",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.movie",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.awardtype"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
