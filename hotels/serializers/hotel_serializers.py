from rest_framework import serializers
from hotels.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'owner', 'name', 'type', 'status', 'stars', 'description',
                  'phone', 'address', 'latitude', 'longitude']

        read_only_fields = ['id', 'owner', 'status', 'stars']


