from rest_framework.generics import CreateAPIView, DestroyAPIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser
from rooms.serializers.room_image_serializers import RoomImageSerializer
from rest_framework.exceptions import PermissionDenied
from accounts.permisions.business import IsBusiness
from rooms.models import RoomImage



class RoomImageCreateAPIView(CreateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = RoomImageSerializer
    parser_classes = [FormParser, MultiPartParser]

    @swagger_auto_schema(
        tags=['room_image'],
        responses={
            201: RoomImageSerializer,
            400: 'bad request',
            404: 'not found'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        room = serializer.validated_data.get('room')

        if room.hotel.owner != self.request.user:
            raise PermissionDenied('room not found')

        serializer.save()



class RoomImageDeleteAPIView(DestroyAPIView):
    permission_classes = [IsBusiness]
    serializer_class = RoomImageSerializer

    @swagger_auto_schema(
        tags=['room_image'],
        responses={
            204: 'no content',
            404: 'not found'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def  get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return RoomImage.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return  RoomImage.objects.none()

        return RoomImage.objects.filter(
            room__hotel__owner=user
        ).order_by('id')




