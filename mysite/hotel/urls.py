from .views import *
from django.urls import path, include
from  rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', ProfileView, basename='profile_list')
router.register(r'city', CityView, basename='city_list')
router.register(r'room', RoomView, basename='room_list')

urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('booking/', BookingCreateAPIView.as_view(), name='booking_edit'),
    path('review/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('reviews/', ReviewListAPIView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),

]
