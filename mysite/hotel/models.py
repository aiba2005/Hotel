from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

TYPE_CHOICES = (
    ('free', 'free'),
    ('booked', 'booked'),
    ('busy', 'busy'),
)

ROOM_CHOICES = (
        ('1kom', '1kom'),
        ('2kom', '2kom'),
        ('domestic', 'domestic'),
    )




class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(18), MaxValueValidator(65)], null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    country_name = models.CharField(max_length=32)
    STATUS_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner')
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='client')


    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class City(models.Model):
   city_name = models.CharField(max_length=32, unique=True)

   def __str__(self):
       return self.city_name


class Room(models.Model):
    room_numbers = models.IntegerField(choices=[(i, str(i)) for i in range(1, 31)])
    status = models.CharField(choices=TYPE_CHOICES, max_length=64, default='free')
    room_types = models.CharField(choices=ROOM_CHOICES, max_length=64, default='1kom')
    description = models.TextField()

    def __str__(self):
       return f'{self.room_numbers}, {self.status},'


class Booking(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    data =models.DateField()
    room = models.ManyToManyField(Room)


    def __str__(self):
        return self.room


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=64)
    city= models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()
    status_hotel = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_name



    def get_avg_rating(self):
        total = self.review.all()
        if total.exists():
            return round(sum([i.stars for i in total]) / total.count(),1)
        return 0


    def get_count_people(self):
        people = self.review.all()
        if people.exists():
            return people.count()
        return 0


class HotelImages(models.Model):
    image = models.ImageField(upload_to='hotel_images', null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)






class Review(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField( null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user








