import pytest
from rest_framework.test import APIClient
from django.urls import reverse



@pytest.mark.django_db
def test_add_room(businessman, hotel):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-create')

    data = {
        'name': 'best_room',
        'description': 'best_room_description',
        'status': 'active',
        'capacity': 4,
        'type': 'deluxe',
        'hotel': hotel.id
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['name'] == 'best_room'



@pytest.mark.django_db
def test_list_room(hotel, multiple_rooms):
    client = APIClient()

    url = reverse('room-list', kwargs={"hotel_id": hotel.id})

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data['count'] == len(multiple_rooms)
    for room_data, room in zip(response.data['results'], multiple_rooms):
        assert room_data['name'] == room.name


@pytest.mark.django_db
def test_update_room(businessman, room):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-update', kwargs={"pk": room.id})

    data = {
        "name": 'changed_name'
    }

    response = client.patch(url, data, format='json')
    print(response.data)

    assert response.status_code == 200
    assert response.data['name'] == 'changed_name'


@pytest.mark.django_db
def test_delete_room(businessman, room):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-delete', kwargs={"pk": room.id})

    response = client.delete(url, format='json')

    assert response.status_code == 204




