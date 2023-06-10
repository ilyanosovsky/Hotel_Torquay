from django.urls import path
from .views import HomePageView, RoomCreateView, GuestCreateView, BookingCreateView, InfoRequestView

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('add_room/', RoomCreateView.as_view(), name='add_room'),
    path('add_guest/', GuestCreateView.as_view(), name='add_guest'),
    path('add_booking/', BookingCreateView.as_view(), name='add_booking'),
    path('add_request/', InfoRequestView.as_view(), name='add_request')
]
