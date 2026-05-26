from rest_framework import serializers
from rooms.models import Room
from .room_image_serializers import RoomImageSerializer



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel', 'name', 'description', 'status', 'capacity', 'type']



class GetRoomSerializer(serializers.ModelSerializer):
    images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'name', 'images', 'description', 'status', 'capacity', 'type']

