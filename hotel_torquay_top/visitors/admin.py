from django.contrib import admin
from .models import Guest, Room, Booking, RoomType, RoomSize, RoomRate
# Register your models here.
admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(RoomType)
admin.site.register(RoomSize)
admin.site.register(RoomRate)
