from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rooms.serializers.room_avbty_serializers import RoomAvailabilitySerializer
from accounts.permisions.business import IsBusiness
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied
from rooms.models import RoomAvailability
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404



class RoomAvailabilityCreateAPIView(CreateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = RoomAvailabilitySerializer

    @swagger_auto_schema(
        tags=['room_avbty'],
        responses={
            201: RoomAvailabilitySerializer,
            400: 'bad request'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        room = serializer.validated_data.get('room')

        if room.hotel.owner != self.request.user:
            raise PermissionDenied("You do not have permission to add availability for this room.")

        serializer.save()



class RoomAvailabilityListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoomAvailabilitySerializer

    @swagger_auto_schema(
        tags=['room_avbty'],
        responses={
            200: RoomAvailabilitySerializer(many=True),
            404: 'not found'
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    def get_queryset(self):
        room_id = self.kwargs.get('room_id')

        return RoomAvailability.objects.filter(
            room__id=room_id
        )


class RoomAvailabilityUpdateAPIView(UpdateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = RoomAvailabilitySerializer

    @swagger_auto_schema(
        tags=['room_avbty'],
        responses={
            200: RoomAvailabilitySerializer,
            404: 'not found',
            400: 'bad request'
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return RoomAvailability.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return RoomAvailability.objects.none()


        return RoomAvailability.objects.filter(
            room__hotel__owner=user
        )


class RoomAvailabilityBlockAPIView(APIView):
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['room_avbty'],
        responses={
            200: 'Room successfully blocked',
            404: 'not found'
        }
    )
    def patch(self, request, pk):
        room_avbty = get_object_or_404(RoomAvailability, pk=pk, room__hotel__owner=request.user)


        if room_avbty.is_blocked():
            return Response({"detail": "room_avbty already blocked"}, status=status.HTTP_400_BAD_REQUEST)

        room_avbty.status = RoomAvailability.StatusChoices.BLOCKED
        room_avbty.save()

        return Response({"detail": "Room successfully blocked"}, status=status.HTTP_200_OK)

