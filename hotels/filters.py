import django_filters
from hotels.models import Hotel



class HotelFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    stars = django_filters.NumberFilter(field_name='stars')
    type = django_filters.CharFilter(field_name='type', lookup_expr='icontains')

    # bu min va max price uchun alohida room degan model qoshish kerak
    # min_price = django_filters.NumberFilter(field_name='')
    # max_price = django_filters.NumberFilter(field_name='')

    # bu uchun alohida HotelAmenities degan model qoshishim kerak
    # amenities = django_filters.CharFilter(field_name='')

    class Meta:
        model = Hotel
        fields = [
            'address',
            'stars',
            'type',
        ]


