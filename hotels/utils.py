from django.db.models import F, FloatField, ExpressionWrapper
from django.db.models.functions import ACos, Cos, Sin, Radians


def filter_by_radius(queryset, lat, lang, radius):
    """
    lat, lng -> user location
    radius -> km
    """

    queryset = queryset.annotate(
        distance=ExpressionWrapper(
            6371 * ACos(
                Cos(Radians(lat)) *
                Cos(Radians(F('latitude'))) *
                Cos(Radians(F('longitude')) - Radians(lang)) +
                Sin(Radians(lat)) *
                Sin(Radians(F('latitude')))
            ),
            output_field=FloatField()
        )
    ).filter(distance__lte=radius)

    return queryset.order_by('distance')