import django_filters
from hotels.models import Hotel



class HotelFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')
    stars = django_filters.NumberFilter(field_name='stars')
    type = django_filters.CharFilter(field_name='type', lookup_expr='icontains')

    min_price = django_filters.NumberFilter(field_name='rooms_prices_main_price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='rooms_prices_main_price', lookup_expr='lte')

    amenities = django_filters.BaseInFilter(field_name='hotelamenity__name', lookup_expr='in')

    class Meta:
        model = Hotel
        fields = [
            'address',
            'stars',
            'type',
            'amenities',
            'min_price',
            'max_price'
        ]


