from rest_framework.views import APIView
from rest_framework.response import Response
from hotels.models import Hotel
from hotels.serializers.hotel_serializers import HotelSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from accounts.permisions.business import IsBusiness, IsAdminOrBusiness
from drf_yasg.utils import swagger_auto_schema
from hotels.utils import filter_by_radius
from hotels.filters import HotelFilter


class AddHotelAPIView(APIView):
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['hotels'],
        request_body=HotelSerializer,
        responses={
            201: HotelSerializer,
            400: "Bad request"
        }
    )
    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetAllHotelsAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['hotels'],
        responses={
            200: HotelSerializer(many=True),
            404: "Not Found"
        }
    )
    def get(self, request):
        queryset = Hotel.objects.all()

        # django-filter
        hotel_filter = HotelFilter(
            request.GET,
            queryset=queryset
        )

        queryset = hotel_filter.qs

        # radius filter
        lang = request.query_params.get('lang')
        lat  = request.query_params.get('lat')
        radius = request.query_params.get('radius')

        if lat and lang and radius:
            queryset = filter_by_radius(queryset=queryset, lat=float(lat), lang=float(lang), radius=float(radius))

        serializer = HotelSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetHotelAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['hotels'],
        responses={
            200: HotelSerializer,
            404: "Not Found"
        }
    )
    def get(self, request, pk):
        try:
            hotel = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response({"error": "hotel not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HotelSerializer(hotel)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateHotelAPIView(APIView):
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['hotels'],
        request_body=HotelSerializer,
        responses={
            200: HotelSerializer,
            400: "Bad request",
            404: "Not found"
        }
    )
    def patch(self, request, pk):
        try:
            hotel = Hotel.objects.get(owner=request.user, pk=pk)
        except Hotel.DoesNotExist:
            return Response({"error": "hotel not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HotelSerializer(hotel, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteHotelAPIView(APIView):
    permission_classes = [IsAdminOrBusiness]

    @swagger_auto_schema(
        tags=['hotels'],
        responses={
            200: "Hotel Successfully deleted",
            404: "Not found"
        }
    )
    def delete(self, request, pk):
        try:
            hotel = Hotel.objects.get(owner=request.user, pk=pk)
        except Hotel.DoesNotExist:
            return Response({"error": "hotel not found"}, status=status.HTTP_404_NOT_FOUND)

        hotel.delete()

        return Response({"message": "Hotel Successfully deleted"}, status=status.HTTP_200_OK)


class GetAllMyHotelsAPIView(APIView):
    permission_classes = [IsBusiness]

    @swagger_auto_schema(
        tags=['hotels'],
        responses={
            200: HotelSerializer(many=True),
            404: "Not found"
        }
    )
    def get(self, request):
        hotels = Hotel.objects.filter(owner=request.user)
        serializer = HotelSerializer(hotels, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

