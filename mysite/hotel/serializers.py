from .models import *
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['last_name', 'first_name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name']


class CitySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']


class HotelImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = ['image']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user', 'room']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_numbers', 'status', 'room_types']


class HotelListSerializer(serializers.ModelSerializer):
    image = HotelImagesSerializer(many=True, read_only=True)
    city = CitySimpleSerializer(many=True)
    class Meta:
        model = Hotel
        fields = ['id', 'city', 'hotel_name', 'image', 'status_hotel']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class HotelDetailSerializer(serializers.ModelSerializer):
    image = HotelImagesSerializer(many=True, read_only=True)
    city = CitySimpleSerializer(many=True)
    class Meta:
        model = Hotel
        fields = ['city', 'hotel_name', 'image', 'status_hotel']