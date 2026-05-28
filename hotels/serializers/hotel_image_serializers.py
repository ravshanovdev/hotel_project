from rest_framework import serializers
from hotels.models import HotelImage, Hotel



class HotelImageSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(
        queryset=Hotel.objects.none()
    )
    class Meta:
        model = HotelImage
        fields = ['id', 'hotel', 'image', 'order']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['hotel'].queryset = Hotel.objects.filter(
                owner=request.user
            )



