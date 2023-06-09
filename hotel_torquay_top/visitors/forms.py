from django import forms
from .models import Guest, Room, Booking, RoomType, RoomSize, RoomRate

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSizeForm(forms.ModelForm):
    class Meta:
        model = RoomSize
        fields = '__all__'

class RoomRateForm(forms.ModelForm):
    class Meta:
        model = RoomRate
        fields = '__all__'