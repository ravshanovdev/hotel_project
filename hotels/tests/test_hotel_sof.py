import pytest
from rest_framework.test import APIClient
from django.urls import reverse



@pytest.mark.django_db
def test_add_special_offer(businessman, hotel):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('hotel-special-offer-create')

    data = {
        "hotel": hotel.id,
        "title": "Special Offer 1",
        "price": 10000,
        "start_time_at": "2024-01-01",
        "end_time_at": "2024-01-10"
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['hotel'] == hotel.id
    assert response.data['price'] == '10000.00'



@pytest.mark.django_db
def test_list_special_offers(hotel, multiple_hotel_sof):
    client = APIClient()

    url = reverse('hotel-special-offer-list', kwargs={"hotel_id": hotel.id})

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert response.data['count'] == len(multiple_hotel_sof)
    assert len(response.data['results']) == len(multiple_hotel_sof)

    for sof in response.data['results']:
        assert sof['hotel'] == hotel.id



@pytest.mark.django_db
def test_update_special_offer(businessman, hotel_sof):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('hotel-special-offer-update', kwargs={"pk": hotel_sof.id})

    data = {
        'title': "changed title"
    }

    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data['title'] == 'changed title'



@pytest.mark.django_db
def test_delete_special_offer(businessman, hotel_sof):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('hotel-special-offer-delete', kwargs={"pk": hotel_sof.id})

    response = client.delete(url, format='json')

    assert response.status_code == 204


