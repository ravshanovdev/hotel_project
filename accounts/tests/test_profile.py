import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_get_my_user_profile(user):
    # ==========================
    # FOR REGULAR USERS
    # ==========================
    client = APIClient()
    client.force_authenticate(user)

    URL = reverse('my-profile')

    response = client.get(URL, format='json')

    assert response.status_code == 200
    assert response.data['user_type'] == 'user'
    assert response.data['is_active'] == False


@pytest.mark.django_db
def test_get_my_business_profile(businessman):
    # ==========================
    # FOR BUSINESS USERS
    # ==========================
    client = APIClient()
    client.force_authenticate(businessman)

    URL = reverse('my-profile')

    response = client.get(URL, format='json')

    assert response.status_code == 200
    assert response.data['user_type'] == 'business'
    assert response.data['is_active'] == False


@pytest.mark.django_db
def test_update_my_profile(user):
    client = APIClient()
    client.force_authenticate(user)

    URL = reverse('update-profile')

    data = {
        'first_name': 'john',
        'last_name': 'wick',
        'city': 'new-york',
    }

    response = client.patch(URL, data, format='multipart')

    assert response.status_code == 200
    assert response.data['first_name'] == 'john'


@pytest.mark.django_db
def test_delete_my_profile(user):
    client = APIClient()
    client.force_authenticate(user)

    URL = reverse('delete-profile')

    response = client.delete(URL, format='json')

    assert response.status_code == 200



