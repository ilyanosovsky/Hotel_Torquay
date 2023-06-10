from typing import Any, Dict, Optional
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Room, RoomType, RoomSize, RoomRate, Guest, Booking, UserRequest
from .forms import RoomForm, RoomTypeForm, RoomSizeForm, RoomRateForm, GuestForm, BookingForm, UserRequestForm
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your views here.

class HomePageView(ListView):
    template_name = 'homepage.html'
    model = Room
    context_object_name = 'all_rooms'

    def get_queryset(self):
        return Room.objects.order_by('room_number')
    
class RoomCreateView(CreateView):
    model = Room
    template_name = 'add_room.html'
    form_class = RoomForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super(RoomCreateView, self).get_context_data(**kwargs)
        context['all_rooms'] = Room.objects.all()
        return context
    
class GuestCreateView(CreateView):
    model = Guest
    template_name = 'add_guest.html'
    form_class = GuestForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def get_context_data(self, **kwargs):
        context = super(GuestCreateView, self).get_context_data(**kwargs)
        context['all_guests'] = Guest.objects.all()
        return context

class BookingCreateView(CreateView):
    model = Booking
    template_name = 'add_booking.html'
    form_class = BookingForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def get_context_data(self, **kwargs):
        context = super(BookingCreateView, self).get_context_data(**kwargs)
        context['all_bookings'] = Booking.objects.all()
        return context 


class InfoRequestView(CreateView):
    model = UserProfile
    template_name = 'add_request.html'
    form_class = UserRequestForm
    success_url = reverse_lazy('add_request')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    
    def get_context_data(self, **kwargs):
        context = super(InfoRequestView, self).get_context_data(**kwargs)
        context['all_requests'] = UserRequest.objects.all()
        return context
