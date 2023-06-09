# Generated by Django 4.2.2 on 2023-06-09 10:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Guest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=20)),
                ("city", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("passport_number", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="RoomSize",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("r_size", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="RoomType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("r_type", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="RoomRate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("daily_rate", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "room_size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="visitors.roomsize",
                    ),
                ),
                (
                    "room_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="visitors.roomtype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_number", models.CharField(max_length=10)),
                ("room_img", models.URLField(default="")),
                ("is_available", models.BooleanField(default=True)),
                ("room_description", models.TextField()),
                (
                    "room_rate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="visitors.roomrate",
                    ),
                ),
                (
                    "room_size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="visitors.roomsize",
                    ),
                ),
                (
                    "room_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="visitors.roomtype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("check_in", models.DateField(default=datetime.date.today)),
                ("check_out", models.DateField()),
                ("is_cancelled", models.BooleanField(default=False)),
                (
                    "guest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="visitors.guest"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="visitors.room"
                    ),
                ),
            ],
        ),
    ]