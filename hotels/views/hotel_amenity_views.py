from hotels.serializers.hotel_amenity_serializers import HotelAmenitySerializer
from hotels.models import HotelAmenity
from rest_framework.generics import CreateAPIView, DestroyAPIView
from drf_yasg.utils import swagger_auto_schema
from accounts.permisions.business import IsBusiness
from rest_framework.exceptions import PermissionDenied


class HotelAmenityCreateAPIView(CreateAPIView):
    serializer_class = HotelAmenitySerializer
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['hotel_amenity'],
        operation_summary="Create a new hotel amenity",
        responses={
            201: HotelAmenitySerializer,
            400: "bad request"
        }
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        hotel = serializer.validated_data['hotel']

        if hotel.owner != self.request.user:
            raise PermissionDenied('You do not own this hotel')

        serializer.save()



class HotelAmenityDeleteAPIView(DestroyAPIView):
    serializer_class = HotelAmenitySerializer
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['hotel_amenity'],
        operation_summary="Delete a hotel amenity"
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self):
        return HotelAmenity.objects.filter(
            hotel__owner=self.request.user
        )




