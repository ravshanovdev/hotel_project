import pytest
from accounts.tests.factory import CustomUserFactory, UserSessionFactory
from accounts.models import CustomUser
from hotels.tests.factorys import HotelFactory, HotelImageFactory, HotelAmenityFactory
from hotels.models import Hotel
import tempfile


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


