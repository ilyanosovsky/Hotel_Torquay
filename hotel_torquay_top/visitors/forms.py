from django import forms
from .models import Guest, Room, Booking, RoomType, RoomSize, RoomRate, UserRequest
from django.utils import timezone

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
        widgets = {
            'check_in' : forms.DateInput(attrs={'type' : 'date'})
        }

    def clean_check_in(self):
        today = timezone.now().date()
        check_in = self.cleaned_data.get('check_in')
        if check_in < today:
            raise forms.ValidationError('Check-In can be only in the future')
        return check_in

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

class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = '__all__'
        exclude = ('user', )