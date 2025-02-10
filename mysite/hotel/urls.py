from .views import *
from django.urls import path, include
from  rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', ProfileView, basename='profile_list')
router.register(r'city', CityView, basename='city_list')
router.register(r'room', RoomView, basename='room_list')
router.register(r'booking', BookingView, basename='booking_list')
router.register(r'hotel', HotelView, basename='hotel_list')
router.register(r'review', ReviewView, basename='review_list')

urlpatterns = [
    path('', include(router.urls)),
]
