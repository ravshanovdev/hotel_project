import pytest
from .factory import CustomUserFactory, UserSessionFactory


@pytest.fixture
def user(db):
    return CustomUserFactory()


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






