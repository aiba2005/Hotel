from .views import *
from django.urls import path, include
from  rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', include(router.urls)),
    path('user/', ProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', ProfileEditAPIView.as_view(), name='user_edit'),

    path('hotels/', HotelCreateAPIView.as_view(), name='hotel_create'),
    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),

    path('booking/', BookingCreateAPIView.as_view(), name='booking_edit'),

    path('review/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewEditAPIView.as_view(), name='review_edit'),

    path('room/', RoomCreateAPIView.as_view(), name='booking_edit'),


    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),
]
