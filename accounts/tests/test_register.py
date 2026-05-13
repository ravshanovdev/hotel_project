import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


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

    assert response.status_code == 201
    assert response.data['message'] == "OTP sent successfully"
    assert response.data['phone'] == '+998889272703'


@pytest.mark.django_db
def test_businessman_can_register(user):
    client = APIClient()

    URL = reverse('register-business')

    data = {
        "user_type": "business",
        # "staff_role": null,
        "phone": "+998889272703",
        "status": "pending",
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

    assert response.status_code == 201
    assert response.data['message'] == "OTP sent successfully"
    assert response.data['phone'] == '+998889272703'


@pytest.mark.django_db
def test_login(user):
    client = APIClient()

    URL = reverse('login')

    user.set_password("1234")
    user.is_active = True
    user.save()

    data = {
        "phone": user.phone,
        "password": "1234",
        "device_id": "1"
    }

    response = client.post(URL, data, format='json')

    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data



@pytest.mark.django_db
def test_logout(user):
    client = APIClient()
    client.force_authenticate(user)

    refresh = RefreshToken.for_user(user)

    URL = reverse('logout')

    data = {
        'refresh': str(refresh)
    }

    response = client.post(URL, data, format='json')

    assert response.status_code == 200
    assert response.data['message'] == "Logged out"

