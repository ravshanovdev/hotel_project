from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FormParser, MultiPartParser
from hotels.serializers.hotel_image_serializers import HotelImageSerializer
from accounts.permisions.business import IsBusiness
from hotels.models import HotelImage
from drf_yasg.utils import swagger_auto_schema


class HotelImageCreateAPIView(CreateAPIView):
    serializer_class = HotelImageSerializer
    permission_classes = [IsBusiness]
    queryset = HotelImage.objects.all()
    parser_classes = [FormParser, MultiPartParser]

    @swagger_auto_schema(
        tags=['hotel_image'],
        request_body=HotelImageSerializer,
        responses={
            201: HotelImageSerializer,
            400: "Bad request",
            403: "permission denied"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        hotel = serializer.validated_data['hotel']

        if hotel.owner != self.request.user:
            raise PermissionDenied("You do not own this hotel")

        serializer.save()


class HotelImageDeleteAPIView(DestroyAPIView):
    serializer_class = HotelImageSerializer
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['hotel_image'],
        responses={
            204: "No content",
            404: "Not found",
            403: "Permission denied"
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        return HotelImage.objects.filter(
            hotel__owner=self.request.user
        )



class HotelImageUpdateAPIView(UpdateAPIView):
    serializer_class = HotelImageSerializer
    permission_classes = [IsBusiness]
    parser_classes = [FormParser, MultiPartParser]

    @swagger_auto_schema(
        tags=['hotel_image'],
        responses={
            200: HotelImageSerializer,
            400: "bad request",
            404: "not found"
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def get_queryset(self):
        return HotelImage.objects.filter(
            hotel__owner=self.request.user
        )




