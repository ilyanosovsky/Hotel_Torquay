# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_torquay.settings')
# import django

# from visitors.models import Guest, Booking, Room, RoomType, RoomSize
# from datetime import datetime, timedelta
# import random
# from faker import Faker

# fake = Faker()

# def create_rooms(number):
#     for r in range(number):
#         room = Room(
#             room_type = random.choice(RoomType.objects.all()),
#             room_size = random.choice(RoomSize.objects.all()),
#             real_cost = random.randint(100, 500)
#         )

#         room.save()

# #create_rooms(20)

# fake = Faker(locale=['en_US', 'it_IT', 'fr_FR'])

# def create_guests(number):

#     for _ in range(number):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         email = fake.email()
#         phone_number = fake.msisdn()

#         guest = Guest(first_name=first_name,
#                       last_name=last_name,
#                       email=email,
#                       phone_number= phone_number)
#         guest.save()

#     print(f"CREATED {number} Guests")

# create_guests(15)

    
