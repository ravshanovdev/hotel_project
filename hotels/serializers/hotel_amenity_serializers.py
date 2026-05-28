from rest_framework import serializers
from hotels.models import HotelAmenity, Hotel


class HotelAmenitySerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(
        queryset=Hotel.objects.none()
    )
    class Meta:
        model = HotelAmenity
        fields = ['id', 'hotel', 'amenity_name', 'icon']
        read_only_fields = ['id']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['hotel'].queryset = Hotel.objects.filter(
                owner=request.user
            )
