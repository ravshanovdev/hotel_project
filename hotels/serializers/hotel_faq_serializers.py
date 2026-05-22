from rest_framework import serializers
from hotels.models import HotelFAQ


class HotelFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFAQ
        fields = ['id', 'hotel', 'question', 'answer', 'section', 'lang']


