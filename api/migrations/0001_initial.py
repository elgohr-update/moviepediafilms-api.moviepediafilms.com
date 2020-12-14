# Generated by Django 3.1.2 on 2020-12-14 00:15

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
            name="Contest",
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
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                ("days_per_movie", models.IntegerField(default=15)),
                (
                    "state",
                    models.CharField(
                        choices=[("C", "Created"), ("L", "Live"), ("F", "Finished")],
                        default="C",
                        max_length=1,
                    ),
                ),
                ("max_recommends", models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name="ContestType",
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
            name="CrewMember",
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
            ],
        ),
        migrations.CreateModel(
            name="Genre",
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
                ("name", models.CharField(max_length=50, unique=True)),
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
                            ("C", "Created"),
                            ("S", "Submitted"),
                            ("R", "Rejected"),
                            ("P", "Published"),
                        ],
                        max_length=1,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "link",
                    models.URLField(
                        error_messages={
                            "unique": "This film already exist on our platform"
                        },
                        unique=True,
                    ),
                ),
                ("runtime", models.FloatField()),
                ("about", models.TextField()),
                ("poster", models.URLField(blank=True, null=True)),
                ("month", models.DateField(blank=True, null=True)),
                ("publish_on", models.DateTimeField(blank=True, null=True)),
                ("jury_rating", models.FloatField(blank=True, default=0, null=True)),
                (
                    "audience_rating",
                    models.FloatField(blank=True, default=0, null=True),
                ),
                ("recommend_count", models.IntegerField(default=0)),
                ("review_count", models.IntegerField(default=0)),
                ("verified", models.BooleanField(blank=True, null=True)),
                (
                    "contest",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movies",
                        to="api.contest",
                    ),
                ),
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="MovieList",
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
                ("frozen", models.BooleanField(default=False)),
                (
                    "contest",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movie_lists",
                        to="api.contest",
                    ),
                ),
                (
                    "liked_by",
                    models.ManyToManyField(
                        blank=True,
                        related_name="liked_lists",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movies",
                    models.ManyToManyField(
                        blank=True, related_name="in_lists", to="api.Movie"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("owner", "name")},},
        ),
        migrations.CreateModel(
            name="Package",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("amount", models.FloatField()),
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
                ("onboarded", models.BooleanField(default=True)),
                ("about", models.TextField(blank=True, null=True)),
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
                ("is_celeb", models.BooleanField(default=False)),
                ("mcoins", models.FloatField(default=0)),
                ("rank", models.IntegerField(default=-1)),
                ("level", models.IntegerField(default=1)),
                ("pop_score", models.FloatField(default=0)),
                ("engagement_score", models.FloatField(default=0)),
                ("reviews_given", models.IntegerField(default=0)),
                (
                    "follows",
                    models.ManyToManyField(
                        blank=True, related_name="followed_by", to="api.Profile"
                    ),
                ),
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
            name="Title",
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
            name="Visits",
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
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.movie"
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.movielist"
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
            name="TopCurator",
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
                ("recommend_count", models.IntegerField(default=0)),
                ("match", models.FloatField(default=0)),
                (
                    "contest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="top_curators",
                        to="api.contest",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TopCreator",
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
                ("recommend_count", models.IntegerField(default=0)),
                ("score", models.FloatField(default=0)),
                (
                    "contest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="top_creators",
                        to="api.contest",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.profile"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="roles",
            field=models.ManyToManyField(
                blank=True, related_name="profiles", to="api.Role"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="titles",
            field=models.ManyToManyField(
                blank=True, related_name="title_holders", to="api.Title"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True, related_name="watchlisted_by", to="api.Movie"
            ),
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
                ("order_id", models.CharField(blank=True, max_length=100, null=True)),
                ("payment_id", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "receipt_number",
                    models.CharField(blank=True, max_length=32, null=True),
                ),
                ("amount", models.FloatField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
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
                ("image", models.URLField(blank=True, null=True)),
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
            name="crew",
            field=models.ManyToManyField(
                related_name="movies", through="api.CrewMember", to="api.Profile"
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(to="api.Genre"),
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
                related_name="movies",
                to="api.order",
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="package",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.package",
            ),
        ),
        migrations.AddField(
            model_name="crewmember",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.movie"
            ),
        ),
        migrations.AddField(
            model_name="crewmember",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.profile"
            ),
        ),
        migrations.AddField(
            model_name="crewmember",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.role"
            ),
        ),
        migrations.CreateModel(
            name="ContestWinner",
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
                ("position", models.IntegerField(blank=True, null=True)),
                (
                    "contest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.contest"
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.profile"
                    ),
                ),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.title"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contest",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.contesttype"
            ),
        ),
        migrations.AddField(
            model_name="contest",
            name="winners",
            field=models.ManyToManyField(
                blank=True, through="api.ContestWinner", to="api.Profile"
            ),
        ),
        migrations.CreateModel(
            name="MovieRateReview",
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
                (
                    "state",
                    models.CharField(
                        choices=[("S", "Published"), ("H", "Blocked")], max_length=1
                    ),
                ),
                ("published_at", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("rating", models.FloatField(blank=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "liked_by",
                    models.ManyToManyField(
                        blank=True,
                        related_name="liked_reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.movie"
                    ),
                ),
            ],
            options={"unique_together": {("movie", "author")},},
        ),
        migrations.CreateModel(
            name="CrewMemberRequest",
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
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("S", "Submitted"),
                            ("A", "Approved"),
                            ("D", "Declined"),
                        ],
                        default="S",
                        max_length=1,
                    ),
                ),
                ("reason", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.movie"
                    ),
                ),
                (
                    "requestor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.role"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="in_crewmemberrequest",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("requestor", "movie", "user", "role")},},
        ),
        migrations.AlterUniqueTogether(
            name="crewmember", unique_together={("movie", "profile", "role")},
        ),
    ]
