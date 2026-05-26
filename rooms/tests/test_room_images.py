import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from hotels.tests.test_hotel_image import generate_image



@pytest.mark.django_db
def test_add_room_image(businessman, room):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-image-create', kwargs={"room_id": room.id})

    data = {
        'room': room.id,
        'image': generate_image()
    }

    response = client.post(url, data, format='multipart')
    print(response.data)

    assert response.status_code == 201
    assert response.data['room'] == room.id



@pytest.mark.django_db
def test_delete_room_image(businessman, room_image):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('room-image-delete', kwargs={"pk": room_image.id})

    response = client.delete(url, format='json')

    assert response.status_code == 204

