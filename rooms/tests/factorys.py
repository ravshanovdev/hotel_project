import factory
from factory.django import DjangoModelFactory
from rooms.models import Room, RoomImage, RoomPrice
from hotels.tests.factorys import HotelFactory


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room


    hotel = factory.SubFactory(HotelFactory)
    name = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('paragraph')
    status = factory.Iterator(Room.StatusChoices.values)
    capacity = factory.Faker('random_int', min=1, max=10)
    type = factory.Iterator(Room.TypeChoices.values)


class RoomImageFactory(DjangoModelFactory):
    class Meta:
        model = RoomImage

    room = factory.SubFactory(RoomFactory, status='active')
    image = factory.django.ImageField(color='black')



class RoomPriceFactory(DjangoModelFactory):
    class Meta:
        model = RoomPrice


    room = factory.SubFactory(RoomFactory, status='active')
    main_price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    week_daily_price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    vocation_price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    holiday_price = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    min_nights = factory.Faker('random_int', min=1, max=10)


