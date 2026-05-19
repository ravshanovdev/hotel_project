import pytest
from accounts.tests.factory import CustomUserFactory, UserSessionFactory
from accounts.models import CustomUser
from hotels.tests.factorys import HotelFactory
from hotels.models import Hotel


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


# Hotel

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







