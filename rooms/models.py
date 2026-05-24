from django.db import models



class Room(models.Model):

    class StatusChoices(models.TextChoices):
        ACTIVE =  'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'
        UNDER_REPAIR =   'under_repair', 'Under Repair'

    class TypeChoices(models.TextChoices):
        STANDARD = 'standard', 'Standard'
        DELUXE = 'deluxe', 'Deluxe'
        SUITE = 'suite', 'Suite'
        FAMILY = 'family', 'Family'
        SINGLE = 'single', 'Single'
        DOUBLE = 'double', 'Double'

    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    capacity = models.IntegerField(default=0)
    type = models.CharField(max_length=20, choices=TypeChoices.choices, default=TypeChoices.STANDARD)


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.room.name



class RoomPrice(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='prices')
    main_price = models.DecimalField(max_digits=10, decimal_places=2)
    week_daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    vocation_price = models.DecimalField(max_digits=10, decimal_places=2)
    holiday_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_nights = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.room.name} -- {self.main_price} so'm"


class RoomAvailability(models.Model):

    class StatusChoices(models.TextChoices):
        EMPTY = 'empty', 'Empty'
        BOOKED = 'booked', 'Booked'
        BLOCKED = 'blocked', 'Blocked'

    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='availability')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.EMPTY)

    def __str__(self):
        return f"{self.room.name} -- {self.status}"

    def is_empty(self):
        return self.status == self.StatusChoices.EMPTY

    def is_booked(self):
        return self.status == self.StatusChoices.BOOKED

    def is_blocked(self):
        return self.status == self.StatusChoices.BLOCKED

    class Meta:
        unique_together = ['room', 'date']