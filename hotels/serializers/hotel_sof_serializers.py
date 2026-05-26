from rest_framework import serializers
from hotels.models import HotelSpecialOffer


class HotelSpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelSpecialOffer
        fields = ['id', 'hotel', 'title', 'price', 'start_time_at', 'end_time_at']
        read_only_fields = ['id']



