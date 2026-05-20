from rest_framework import serializers
from hotels.models import HotelImage



class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['id', 'hotel', 'image', 'order']




