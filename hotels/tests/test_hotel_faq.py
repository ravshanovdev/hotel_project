import pytest
from rest_framework.test import APIClient
from django.urls import reverse



@pytest.mark.django_db
def test_create_hotel_faq(businessman, hotel):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('hotel-faq-create')

    data = {
        'hotel': hotel.id,
        'section': 'breakfast',
        'question': 'Is breakfast included?',
        'answer': 'Yes, breakfast is included in the room rate.'
    }

    response = client.post(url, data, format='json')

    assert response.status_code == 201
    assert response.data['hotel'] == hotel.id
    assert response.data['section'] == 'breakfast'



@pytest.mark.django_db
def test_list_hotel_faq(hotel, multiple_hotel_faq):
    client = APIClient()

    url = reverse('hotel-faq-list', kwargs={"hotel_id": hotel.id})

    response = client.get(url, format='json')

    assert response.status_code == 200
    assert len(response.data) == len(multiple_hotel_faq)
    for faq in response.data:
        assert faq['hotel'] == hotel.id



@pytest.mark.django_db
def test_update_hotel_faq(businessman, hotel_faq):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('hotel-faq-update', kwargs={'pk': hotel_faq.id})

    data = {
        'section': "transfer"
    }

    response = client.patch(url, data, format='json')

    assert response.status_code == 200
    assert response.data['section'] == 'transfer'



@pytest.mark.django_db
def test_delete_hotel_faq(businessman, hotel_faq):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('hotel-faq-delete', kwargs={'pk': hotel_faq.id})

    response = client.delete(url, format='json')

    assert response.status_code == 204












