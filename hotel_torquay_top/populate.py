import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_torquay.settings')
import django

from visitors.models import Guest, Booking, Room, RoomType, RoomSize
from datetime import datetime, timedelta
import random
# from faker import Faker

# fake = Faker()

def create_rooms(number):
    for r in range(number):
        room = Room(
            room_type = random.choice(RoomType.objects.all()),
            room_size = random.choice(RoomSize.objects.all()),
            real_cost = random.randint(100, 500)
        )

        room.save()

create_rooms(20)