# Generated by Django 4.2.2 on 2023-06-09 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0002_rename_r_size_roomsize_room_size_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="roomrate",
            old_name="daily_rate",
            new_name="room_rate",
        ),
    ]