from rest_framework import serializers
from rooms.models import RoomAvailability, Room



class RoomAvailabilitySerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.none()
    )

    class Meta:
        model = RoomAvailability
        fields = ['id', 'room', 'date', 'status']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['room'].queryset = Room.objects.filter(
                hotel__owner=request.user
            )
