from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from hotels.models import HotelFAQ
from drf_yasg.utils import swagger_auto_schema
from accounts.permisions.business import IsBusiness
from hotels.serializers.hotel_faq_serializers import HotelFAQSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny


class HotelFAQCreateAPIView(CreateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = HotelFAQSerializer

    @swagger_auto_schema(
        tags=['hotel_faq'],
        responses={
            201: HotelFAQSerializer,
            400: 'bad request',
            404: 'not found'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        hotel = serializer.validated_data['hotel']

        if hotel.owner != self.request.user:
            raise PermissionDenied('you do not own this hotel.')

        serializer.save()


class HotelFAQListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = HotelFAQSerializer

    @swagger_auto_schema(
        tags=['hotel_faq'],
        responses={
            200: HotelFAQSerializer(many=True),
            404: 'not found'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        hotel_id = self.kwargs['hotel_id']
        return HotelFAQ.objects.filter(hotel__id=hotel_id)


class HotelFAQUpdateAPIView(UpdateAPIView):
    permission_classes = [IsBusiness]
    serializer_class = HotelFAQSerializer


    @swagger_auto_schema(
        tags=['hotel_faq'],
        responses={
            200: HotelFAQSerializer,
            404: 'not found',
            400: 'bad request'
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return HotelFAQ.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return HotelFAQ.objects.none()

        return HotelFAQ.objects.filter(
            hotel__owner=user
        )



class HotelFAQDeleteAPIView(DestroyAPIView):
    permission_classes = [IsBusiness]
    serializer_class = HotelFAQSerializer

    @swagger_auto_schema(
        tags=['hotel_faq'],
        responses={
            204: 'no content',
            404: 'not found'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):

        if getattr(self, 'swagger_fake_view', False):
            return HotelFAQ.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return HotelFAQ.objects.none()

        return HotelFAQ.objects.filter(
            hotel__owner=user
        )


