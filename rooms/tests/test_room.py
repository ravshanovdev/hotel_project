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






