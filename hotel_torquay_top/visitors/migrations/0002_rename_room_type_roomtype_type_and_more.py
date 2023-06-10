# Generated by Django 4.2.2 on 2023-06-10 20:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("visitors", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="roomtype",
            old_name="room_type",
            new_name="type",
        ),
        migrations.RemoveField(
            model_name="room",
            name="room_description",
        ),
        migrations.RemoveField(
            model_name="room",
            name="room_number",
        ),
        migrations.RemoveField(
            model_name="roomsize",
            name="room_size",
        ),
        migrations.AddField(
            model_name="roomsize",
            name="size",
            field=models.CharField(default="", max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="roomtype",
            name="room_description",
            field=models.TextField(default=" "),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="booking",
            name="check_out",
            field=models.DateField(default=datetime.date(2023, 6, 11)),
        ),
        migrations.AlterField(
            model_name="booking",
            name="guest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="guest",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="room",
                to="visitors.room",
            ),
        ),
        migrations.AlterField(
            model_name="roomrate",
            name="room_size",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="room_size",
                to="visitors.roomsize",
            ),
        ),
        migrations.AlterField(
            model_name="roomrate",
            name="room_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="room_type",
                to="visitors.roomtype",
            ),
        ),
    ]