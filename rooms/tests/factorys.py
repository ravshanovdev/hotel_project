import factory
from factory.django import DjangoModelFactory
from rooms.models import Room
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




