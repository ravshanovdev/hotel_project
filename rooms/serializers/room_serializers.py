from rest_framework import serializers
from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'name', 'description', 'status', 'capacity', 'type']


    def validate(self, attrs):
        hotel = attrs.get('hotel')
        user = self.context['request'].user

        if hotel.owner != user:
            raise serializers.ValidationError('hot not found.')

        return attrs
