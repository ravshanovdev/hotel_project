import pytest
from accounts.tests.factory import CustomUserFactory, UserSessionFactory
from accounts.models import CustomUser
from hotels.tests.factorys import (HotelFactory, HotelImageFactory, HotelAmenityFactory, HotelFAQFactory,
                                   HotelSpecialOfferFactory)
from hotels.models import Hotel
import tempfile
from rooms.tests.factorys import RoomFactory, RoomImageFactory, RoomPriceFactory, RoomAvailabilityFactory




@pytest.fixture(autouse=True)
def temp_media_root(settings):
    with tempfile.TemporaryDirectory() as temp_dir:
        settings.MEDIA_ROOT = temp_dir
        yield


# accounts(CustomUser)

@pytest.fixture
def user(db):
    return CustomUserFactory()


@pytest.fixture
def businessman(db):
    return CustomUserFactory(user_type=CustomUser.UserType.BUSINESS)

@pytest.fixture
def admin_user(db):
    return UserSessionFactory(is_staff=True, is_superuser=True, is_active=True)


@pytest.fixture
def user_session(db, user):
    return UserSessionFactory(user=user)


@pytest.fixture
def three_user_sessions(db, user):
    return UserSessionFactory.create_batch(3)


@pytest.fixture
def five_user_sessions(db, user):
    return UserSessionFactory.create_batch(5)


# hotels(Hotel)

@pytest.fixture
def hotel(db, businessman):
    return HotelFactory(owner=businessman)


@pytest.fixture
def multiple_hotels_one_owner(db, businessman):
    return HotelFactory.create_batch(5, status=Hotel.StatusChoices.ACTIVE,
                                     owner=businessman)

@pytest.fixture
def multiple_hotels(db):
    return HotelFactory.create_batch(5, status=Hotel.StatusChoices.ACTIVE)


# hotels(HotelImage)

@pytest.fixture
def hotel_image(db, hotel):
    return HotelImageFactory(hotel=hotel)


@pytest.fixture
def multiple_hotel_image(db):
    return HotelImageFactory.create_batch(5)



# hotels(HotelAmenity)

@pytest.fixture
def hotel_amenity(db, hotel):
    return HotelAmenityFactory(hotel=hotel)


@pytest.fixture
def multiple_hotel_amenity(db, hotel):
    return HotelAmenityFactory.create_batch(5, hotel=hotel)


# hotels(HotelFAQ)

@pytest.fixture
def hotel_faq(db, hotel):
    return HotelFAQFactory(hotel=hotel)


@pytest.fixture
def multiple_hotel_faq(db, hotel):
    return HotelFAQFactory.create_batch(5, hotel=hotel)


# hotels(HotelSpecialOffer)

@pytest.fixture
def hotel_sof(db, hotel):
    return HotelSpecialOfferFactory(hotel=hotel)


@pytest.fixture
def multiple_hotel_sof(db, hotel):
    return HotelSpecialOfferFactory.create_batch(5, hotel=hotel)


# rooms(Room)

@pytest.fixture
def room(db, hotel):
    return RoomFactory(hotel=hotel)


@pytest.fixture
def multiple_rooms(db, hotel):
    return RoomFactory.create_batch(5, hotel=hotel, status='active')


# room(RoomImage)

@pytest.fixture
def room_image(db, room):
    return RoomImageFactory(room=room)


@pytest.fixture
def multiple_room_images(db, room):
    return RoomImageFactory.create_batch(5, room=room)



# room(RoomPrice)

@pytest.fixture
def room_price(db, room):
    return RoomPriceFactory(room=room)


@pytest.fixture
def multiple_room_prices(db, room):
    return RoomPriceFactory.create_batch(5, room=room)


# room(RoomAvailability

@pytest.fixture
def room_avbty(db, room):
    return RoomAvailabilityFactory(room=room)


@pytest.fixture
def multiple_room_avbty(db, room):
    return RoomAvailabilityFactory.create_batch(5, room=room)







