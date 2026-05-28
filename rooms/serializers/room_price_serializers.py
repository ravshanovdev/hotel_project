from rest_framework import serializers
from rooms.models import RoomPrice, Room



class RoomPriceSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.none()
    )

    class Meta:
        model = RoomPrice
        fields = ['id', 'room', 'main_price', 'week_daily_price', 'vocation_price', 'holiday_price', 'min_nights']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['room'].queryset = Room.objects.filter(
                hotel__owner=request.user
            )




