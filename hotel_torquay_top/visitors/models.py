from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Room(models.Model):
    room_img = models.URLField(default = '')
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    room_size = models.ForeignKey('RoomSize', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.room_type} {self.room_size}'
    
class Booking(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    check_in = models.DateField(default=date.today)
    check_out = models.DateField(default=(date.today() + timedelta(days=1)))
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.room} room for {self.guest.first_name} {self.guest.last_name}"

    
class RoomType(models.Model):
    type = models.CharField(max_length=20)
    room_description = models.TextField()

    def __str__(self):
        return self.type
    
    
class RoomSize(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    
class RoomRate(models.Model):
    room_rate = models.DecimalField(max_digits=10, decimal_places=2)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='room_type')
    room_size = models.ForeignKey(RoomSize, on_delete=models.CASCADE, related_name='room_size')

    def __str__(self):
        return f"{self.room_type} {self.room_size} {self.room_rate}"
    
class UserRequest(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return f"Request from {self.first_name} {self.last_name}"
