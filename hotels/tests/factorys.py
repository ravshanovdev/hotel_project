from factory.django import DjangoModelFactory
import factory
from hotels.models import Hotel, HotelImage, HotelAmenity
from accounts.tests.factory import CustomUserFactory
from accounts.models import CustomUser


class HotelFactory(DjangoModelFactory):
    class Meta:
        model = Hotel

    owner = factory.SubFactory(CustomUserFactory, user_type=CustomUser.UserType.BUSINESS, is_active=True)
    name = factory.Sequence(lambda x: f"NewStar00{x}")
    type = factory.Faker('random_element', elements=[choice[0] for choice in Hotel.TypeChoices.choices])
    status = Hotel.StatusChoices.IN_MODERATION
    stars = factory.Faker('random_int', min=1, max=5)
    description = factory.Faker('paragraph')
    phone = factory.Sequence(lambda x: f"+99888927270{x}")
    address = factory.Faker('address')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')


class HotelImageFactory(DjangoModelFactory):
    class Meta:
        model = HotelImage

    hotel = factory.SubFactory(HotelFactory)
    image = factory.django.ImageField(color='blue')
    order = factory.Sequence(lambda x: x)


class HotelAmenityFactory(DjangoModelFactory):
    class Meta:
        model = HotelAmenity

    hotel = factory.SubFactory(HotelFactory)
    amenity_name = factory.Sequence(lambda x: f"Amenity {x}")
    icon = factory.Faker('image_url')
