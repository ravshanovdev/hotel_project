import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image


def generate_image():
    file = BytesIO()

    image = Image.new('RGB', (100, 100), color='red')
    image.save(file, 'JPEG')
    file.seek(0)

    return SimpleUploadedFile(
        'test.jpg',
        file.read(),
        content_type='image/jpeg'
    )



@pytest.mark.django_db
def test_add_hotel_image(businessman, hotel):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('add-hotel-image')

    data = {
        'hotel': hotel.id,
        'image': generate_image(),
        'order': 1
    }

    response = client.post(url, data, format='multipart')

    assert response.status_code == 201
    assert response.data['hotel'] == hotel.id



@pytest.mark.django_db
def test_delete_hotel_image(businessman, hotel_image):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('delete-hotel-image', kwargs={"pk": hotel_image.id})

    response = client.delete(url, format='json')

    assert response.status_code == 204


@pytest.mark.django_db
def test_update_hotel_image(businessman, hotel, hotel_image):
    client = APIClient()
    client.force_authenticate(businessman)

    url = reverse('update-hotel-image', kwargs={"pk": hotel_image.id})

    data = {
        'hotel': hotel.id,
        'order': 2
    }

    response = client.patch(url, data, format='multipart')

    assert response.status_code == 200
    assert response.data['order'] == 2
    assert response.data['hotel'] == hotel.id
