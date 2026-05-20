from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models



class Hotel(models.Model):

    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', "Active"
        INACTIVE = 'inactive', 'Inactive'
        IN_MODERATION = 'in moderation', 'In Moderation'

    class TypeChoices(models.TextChoices):
        HOTEL = 'hotel', 'Hotel'
        HOSTEL = 'hostel', 'Hostel'
        APART = 'apart', 'Apart'
        RESORT = 'resort', 'Resort'
        GUEST_HOUSE = 'guest house', 'Guest House'

    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150, choices=TypeChoices.choices, default=TypeChoices.HOTEL)
    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.IN_MODERATION)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    description = models.TextField()
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.hotel.name


class HotelAmenity(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='amenities')
    amenity_name = models.CharField(max_length=150)
    icon = models.URLField()

    def __str__(self):
        return self.amenity_name


class HotelFAQ(models.Model):
    class SectionChoices(models.TextChoices):
        BREAKFAST = 'breakfast', 'Breakfast'
        TRANSFER = 'transfer', 'Transfer'
        LOCATION = 'location', 'Location'
        PAYMENT = 'payment', 'Payment'

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='faqs')
    question = models.TextField()
    answer = models.TextField()
    section = models.CharField(max_length=50, choices=SectionChoices.choices)
    lang = models.CharField(max_length=5, choices=[('uz','UZ'),('ru','RU'),('en','EN')],
                                    default='uz')

    def __str__(self):
        return self.question


class HotelSpecialOffer(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='special_offers')
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time_at = models.DateField()
    end_time_at = models.DateField()

    def __str__(self):
        return self.title

