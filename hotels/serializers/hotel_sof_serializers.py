from rest_framework import serializers
from hotels.models import HotelSpecialOffer


class HotelSpecialOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelSpecialOffer
        fields = ['id', 'hotel', 'title', 'price', 'start_time_at', 'end_time_at']
        read_only_fields = ['id']

    def validate(self, attrs):
        user = self.context['request'].user
        hotel = attrs.get('hotel')

        if hotel is None:
            return attrs

        if hotel.owner != user:
            raise serializers.ValidationError('hotel not found')

        return attrs


