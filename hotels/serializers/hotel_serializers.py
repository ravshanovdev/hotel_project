from rest_framework import serializers
from hotels.models import Hotel
from accounts.validators.validator import phone_validator


class HotelSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True, validators=[phone_validator])
    class Meta:
        model = Hotel
        fields = ['id', 'owner', 'name', 'type', 'status', 'stars', 'description',
                  'phone', 'address', 'latitude', 'longitude']

        read_only_fields = ['id', 'owner', 'status']


