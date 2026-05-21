from rest_framework import serializers
from hotels.models import HotelAmenity


class HotelAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAmenity
        fields = ['id', 'hotel', 'amenity_name', 'icon']
        read_only_fields = ['id']

