from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'country_name']


class CityListSerializer(serializers.ModelSerializer):
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
        fields = ['hotel_image']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user' , 'booking_hotel',
                  'departure', 'check_in', 'adults', 'children', 'room', 'created_date']



class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']



class RoomSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['room_numbers', 'room_images', 'status', 'room_types', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'hotel', 'stars', 'parent', 'text', 'created_date']


class ReviewHotelSerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()
    class Meta:
        model = Review
        fields = ['user',  'text']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelImagesSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people =serializers.SerializerMethodField()
    review = ReviewHotelSerializer(many=True, read_only=True)
    # get_avg_count_person = serializers.SerializerMethodField()
    # get_avg_person = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['id', 'city', 'hotel_name', 'hotel_image',
                  'status_hotel', 'get_avg_rating', 'get_count_people', 'review']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


    #
    # def get_avg_person(self, obj):
    #     return obj.get_avg_person()

    # def get_avg_count_person(self, obj):
    #     return obj.get_avg_count_person()


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_image = HotelImagesSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    room_image = RoomImageSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    review = ReviewHotelSerializer(many=True, read_only=True)
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Hotel
        fields = ['city', 'hotel_name', 'room_image', 'hotel_image','status_hotel',
                  'get_avg_rating', 'get_count_people', 'review', 'created_date']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class CityDetailSerializer(serializers.ModelSerializer):
    hotel_city = HotelListSerializer(many=True, read_only=True)
    class Meta:
        model = City
        fields = ['city_name', 'hotel_city' ]


class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = [ 'hotel_name', 'country', 'city',
                  'status_hotel', 'description']
