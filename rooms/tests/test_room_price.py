import pytest
from rest_framework.test import APIClient
from django.urls import reverse



@pytest.mark.django_db
def test_create_room_price(businessman, room):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-price-create')

    data = {
        'room': room.id,
        'main_price': 100.00,
        'week_daily_price': 80.00,
        'vocation_price': 120.00,
        'holiday_price': 150.00,
        'min_nights': 2
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['room'] == room.id
    assert response.data['main_price'] == "100.00"


@pytest.mark.django_db
def test_list_roo_prices(room, multiple_room_prices):
    client = APIClient()

    url = reverse("room-price-list", kwargs={"room_id": room.id})

    response = client.get(url, format='json')


    assert response.status_code == 200
    assert len(response.data['results']) == len(multiple_room_prices)
    for item in response.data['results']:
        assert item['room'] == room.id



@pytest.mark.django_db
def test_update_roo_price(businessman, room_price):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-price-update', kwargs={"pk": room_price.id})

    data = {
        "main_price": 154.70
    }

    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data['main_price'] == "154.70"













