import pytest
from rest_framework.test import APIClient
from django.urls import reverse



@pytest.mark.django_db
def test_register_regular_user(user):
    client = APIClient()

    URL = reverse('register')

    data = {
          "user_type": "user",
          # "staff_role": null,
          "phone": "+998889272703",
          "status": "approved",
          "first_name": "somebody",
          "last_name": "somebodyovich",
          "city": "tokio",
          # "district": "",
          # "email": null,
          # "birth_date": null,
          "language": "uz",
          # "image": null,
          # "company": "",
          "inn": 123456789,
          "stir": "lalalalalalla",
          # "legal_address": "",
        "password": "asajaksjdhaj6789",
        "password2": "asajaksjdhaj6789"
    }

    response = client.post(URL, data, format='json')
    print(response.data)
    assert response.status_code == 201
