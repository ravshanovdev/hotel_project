from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from drf_yasg.utils import swagger_auto_schema
from rooms.serializers.room_serializers import RoomSerializer
from rooms.models import Room
from accounts.permisions.business import IsBusiness
from rest_framework.permissions import AllowAny



class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['room'],
        responses={
            201: RoomSerializer,
            400: 'bad request'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class RoomListAPIView(ListAPIView):
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags = ['room'],
        responses={
            200: RoomSerializer(many=True),
            404: 'not found'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')

        return Room.objects.filter(
            hotel__id=hotel_id, status='active'
        )



class RoomUpdateAPIView(UpdateAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['room'],
        responses={
            200: RoomSerializer,
            400: 'bad request',
            404: 'not found'
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return Room.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return Room.objects.none()

        return Room.objects.filter(
            hotel__owner=user
        )



class RoomDeleteAPIView(DestroyAPIView):
    serializer_class = RoomSerializer
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['room'],
        responses={
            204: 'no content',
            404: 'not found'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return Room.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return Room.objects.none()

        return Room.objects.filter(
            hotel__owner=user
        )
