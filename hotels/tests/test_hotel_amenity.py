from rest_framework.test import APIClient
import pytest
from django.urls import reverse




@pytest.mark.django_db
def test_add_hotel_amenity(businessman, hotel):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('add-hotel-amenity')

    data = {
        'hotel': hotel.id,
        'icon': 'https://example.com/icon.png',
        'amenity_name': "best"
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['amenity_name'] == 'best'
    assert response.data['icon'] == 'https://example.com/icon.png'


@pytest.mark.django_db
def test_delete_amenity(businessman, hotel_amenity):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('delete-hotel-amenity', kwargs={'pk': hotel_amenity.id})

    response = client.delete(url)

    assert response.status_code == 204

















