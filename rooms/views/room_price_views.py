from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from drf_yasg.utils import swagger_auto_schema
from accounts.permisions.business import IsBusiness
from rooms.serializers.room_price_serializers import RoomPriceSerializer
from rooms.models import RoomPrice
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny



class RoomPriceCreateAPIView(CreateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = RoomPriceSerializer

    @swagger_auto_schema(
        tags=['room_price'],
        responses={
            201: RoomPriceSerializer,
            400: 'bad request'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        room = serializer.validated_data.get('room')

        if room.hotel.owner != self.request.user:
            raise PermissionDenied('this room not belong to you.!')

        serializer.save()



class RoomPriceListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RoomPriceSerializer

    @swagger_auto_schema(
        tags=['room_price'],
        responses={
            200: RoomPriceSerializer(many=True),
            404: 'not found'
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):

        room_id = self.kwargs.get('room_id')

        return RoomPrice.objects.filter(
            room__id=room_id
        )


class RoomPriceUpdateAPIView(UpdateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = RoomPriceSerializer

    @swagger_auto_schema(
        tags=['room_price'],
        responses={
            200: RoomPriceSerializer,
            400: 'bad request',
            404: 'not found'
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return RoomPrice.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return RoomPrice.objects.none()

        return RoomPrice.objects.filter(
            room__hotel__owner=user
        )
