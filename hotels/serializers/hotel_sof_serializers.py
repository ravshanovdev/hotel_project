from rest_framework import serializers
from hotels.models import HotelSpecialOffer, Hotel


class HotelSpecialOfferSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(
        queryset=Hotel.objects.none()
    )
    class Meta:
        model = HotelSpecialOffer
        fields = ['id', 'hotel', 'title', 'price', 'start_time_at', 'end_time_at']
        read_only_fields = ['id']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['hotel'].queryset = Hotel.objects.filter(
                owner=request.user
            )

