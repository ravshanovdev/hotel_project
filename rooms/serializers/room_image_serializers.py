from rest_framework import serializers
from rooms.models import RoomImage



class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'room', 'image']



