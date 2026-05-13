import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.utils.otp import send_otp
from django.core.cache import cache


@pytest.mark.django_db
def test_verify_otp(user):
    client = APIClient()

    send_otp(user.phone)

    code = cache.get(f"otp:{user.phone}")

    url = reverse('verify-otp')
    data = {
        'device_id': '1',
        'phone': user.phone,
        'code': str(code)
    }

    response = client.post(url, data, format='json')

    print(response)
    print(response.data)

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data
    assert response.data['user_id'] == user.id



@pytest.mark.django_db
def test_send_otp(user):
    client = APIClient()
    client.force_authenticate(user)

    URL = reverse('resent-otp')

    data = {
        "phone": user.phone
    }

    response = client.post(URL, data, format='json')

    assert response.status_code == 200
    assert response.data['message'] == 'OTP resent successfully'





