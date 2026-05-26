from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from hotels.serializers.hotel_sof_serializers import HotelSpecialOfferSerializer
from drf_yasg.utils import swagger_auto_schema
from accounts.permisions.business import IsBusiness
from rest_framework.permissions import AllowAny
from hotels.models import HotelSpecialOffer
from rest_framework.exceptions import PermissionDenied



class HotelSpecialOfferCreateAPIView(CreateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = HotelSpecialOfferSerializer

    @swagger_auto_schema(
        tags=['hotel_special_offer'],
        responses={
            201: HotelSpecialOfferSerializer,
            400: 'bad request',
            404: "not found"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        hotel = serializer.validated_data['hotel']

        if hotel.owner != self.request.user:
            raise PermissionDenied('Hotel not found.')

        serializer.save()


class HotelSpecialOfferListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelSpecialOfferSerializer

    @swagger_auto_schema(
        tags=['hotel_special_offer'],
        responses={
            200: HotelSpecialOfferSerializer(many=True),
            404: 'not found'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')

        return HotelSpecialOffer.objects.filter(
            hotel__id=hotel_id
        )


class HotelSpecialOfferUpdateAPIView(UpdateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = HotelSpecialOfferSerializer

    @swagger_auto_schema(
        tags=['hotel_special_offer'],
        responses={
            200: HotelSpecialOfferSerializer,
            400: 'bad request',
            404: 'not found'
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', None):
            return HotelSpecialOffer.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return HotelSpecialOffer.objects.none()

        return HotelSpecialOffer.objects.filter(
            hotel__owner=user
        )



class HotelSpecialOfferDeleteAPIView(DestroyAPIView):
    permission_classes = [IsBusiness]
    serializer_class = HotelSpecialOfferSerializer

    @swagger_auto_schema(
        tags=['hotel_special_offer'],
        responses={
            204: 'no content',
            404: 'not found'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', None):
            return HotelSpecialOffer.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return HotelSpecialOffer.objects.none()

        return HotelSpecialOffer.objects.filter(
            hotel__owner=user
        )

