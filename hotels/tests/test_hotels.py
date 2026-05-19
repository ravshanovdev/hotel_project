from rest_framework.test import APIClient
from django.urls import reverse
import pytest



@pytest.mark.django_db
def test_businessman_can_add_hotel(businessman):
    client = APIClient()
    client.force_authenticate(businessman)

    URL = reverse('add-hotel')

    data = {
        "name": "NewStar",
        'type': "hotel",
        'stars': 4,
        "description": "A new hotel in the city center.",
        "phone": "+998901234567",
        "address": "123 Main St, Cityville",
        "latitude": 40.7128,
        "longitude": -74.0060
    }

    response = client.post(URL, data, format='json')

    assert response.status_code == 201
    assert response.data['stars'] == 4
    assert response.data['name'] == 'NewStar'


@pytest.mark.django_db
def test_regular_user_can_not_add_hotel(user):
    client = APIClient()
    client.force_authenticate(user)

    URL = reverse('add-hotel')

    data = {
        "name": "NewStar",
        'type': "hotel",
        'stars': 4,
        "description": "A new hotel in the city center.",
        "phone": "+998901234567",
        "address": "123 Main St, Cityville",
        "latitude": 40.7128,
        "longitude": -74.0060
    }

    response = client.post(URL, data, format='json')

    assert response.status_code == 403



@pytest.mark.django_db
def test_list_hotels(multiple_hotels):
    client = APIClient()
    # client.force_authenticate(user)

    url = reverse('all-hotels')

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert len(response.data) == len(multiple_hotels)


@pytest.mark.django_db
def test_detail_hotel(hotel):
    client = APIClient()

    url = reverse('detail-hotel', kwargs={'pk': hotel.id})

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data['owner'] == hotel.owner.id
    assert response.data['name'] == hotel.name



@pytest.mark.django_db
def test_get_my_hotels(businessman, multiple_hotels_one_owner):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('all-my-hotels')

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert len(response.data) == len(multiple_hotels_one_owner)


@pytest.mark.django_db
def test_delete_hotel(businessman, hotel):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('delete-hotel', kwargs={"pk": hotel.id})

    response = client.delete(url, format='json')

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_hotel(businessman, hotel):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('update-hotel', kwargs={'pk': hotel.id})

    data = {
        "name": "changed",
    }

    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data['name'] == 'changed'

