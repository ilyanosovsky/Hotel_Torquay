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
            'check_in' : forms.DateInput(attrs={'type' : 'date'}),
            'check_out' : forms.DateInput(attrs={'type' : 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        today = timezone.now().date()
        check_in = self.cleaned_data.get('check_in')
        check_out = self.cleaned_data.get('check_out')
        if check_in and check_out:
            if check_in < today:
                raise forms.ValidationError('Check-In can only be in the future')
            if check_out == today:
                raise forms.ValidationError('Check-Out cant be on the same date')
            
            room = self.cleaned_data.get('room')
            if not room.is_available:
                raise forms.ValidationError('Room is currently unavailable. Please choose another room type...')
            
        return cleaned_data



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

GuestFormSet = forms.modelformset_factory(Guest, form=GuestForm, extra=1)