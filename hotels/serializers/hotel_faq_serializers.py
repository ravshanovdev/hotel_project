from rest_framework import serializers
from hotels.models import HotelFAQ, Hotel


class HotelFAQSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(
        queryset=Hotel.objects.none()
    )
    class Meta:
        model = HotelFAQ
        fields = ['id', 'hotel', 'question', 'answer', 'section', 'lang']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['hotel'].queryset = Hotel.objects.filter(
                owner=request.user
            )
