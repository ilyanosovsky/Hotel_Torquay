from django.db import models
import datetime

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
        return self.first_name + ' ' + self.last_name
    
class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_img = models.URLField(default = '')
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    room_size = models.ForeignKey('RoomSize', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    room_description = models.TextField()

    def __str__(self):
        return self.room_number
    
class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField(default=datetime.date.today)
    check_out = models.DateField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.guest.first_name + ' ' + self.guest.last_name + ' ' + self.room.room_number
    
class RoomType(models.Model):
    room_type = models.CharField(max_length=20)

    def __str__(self):
        return self.room_type
    
    
class RoomSize(models.Model):
    room_size = models.CharField(max_length=20)

    def __str__(self):
        return self.room_size
    
class RoomRate(models.Model):
    room_rate = models.DecimalField(max_digits=10, decimal_places=2)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_size = models.ForeignKey(RoomSize, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.room_type} {self.room_size} {self.room_rate}"