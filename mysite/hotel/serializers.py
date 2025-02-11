from .models import *
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'country_name']


class ProfileBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['last_name', 'first_name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image']


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
        fields = ['user' , 'booking',
                  'departure', 'check_in', 'adults', 'children', 'room', 'created_date']


class BookingSimpleSerializer(serializers.ModelSerializer):
    user = ProfileBookingSerializer()
    class Meta:
        model = Booking
        fields = ['user' , 'check_in',
                  'departure']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_numbers', 'status', 'room_types', 'price']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'hotel', 'stars', 'parent', 'text', 'created_date']

class HotelListSerializer(serializers.ModelSerializer):
    image = HotelImagesSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people =serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['id', 'country', 'city', 'hotel_name', 'image', 'status_hotel', 'get_avg_rating', 'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class HotelDetailSerializer(serializers.ModelSerializer):
    image = HotelImagesSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    booking = BookingSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['city', 'hotel_name', 'image',
                  'status_hotel','created_date', 'booking']