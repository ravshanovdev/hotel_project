import pytest
from rest_framework.test import APIClient
from django.urls import reverse



@pytest.mark.django_db
def test_create_room_avbty(businessman, room):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-avbty-create')

    data = {
        'room': room.id,
        'date': '2024-07-01',
        'status': 'empty'
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['room'] ==room.id
    assert response.data['status'] == 'empty'



@pytest.mark.django_db
def test_list_room_avbty(businessman, room, multiple_room_avbty):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-avbty-list', kwargs={'room_id': room.id})

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert len(response.data['results']) == len(multiple_room_avbty)
    for room_avb in response.data['results']:
        assert room_avb['room'] == room.id



@pytest.mark.django_db
def test_block_room_avbty(businessman, room_avbty):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-avbty-block', kwargs={'pk': room_avbty.id})

    response = client.patch(url, format='json')

    assert response.status_code == 200
    assert response.data['detail'] == 'Room successfully blocked'



@pytest.mark.django_db
def test_update_room_avbty(businessman, room_avbty):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-avbty-update', kwargs={'pk': room_avbty.id})

    data = {
        'status': 'booked'
    }

    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data['status'] == 'booked'












