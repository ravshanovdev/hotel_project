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

