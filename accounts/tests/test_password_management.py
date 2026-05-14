import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.core.cache import cache


@pytest.mark.django_db
def test_change_password(user):
    client = APIClient()
    client.force_authenticate(user)

    URL = reverse('change-password')

    user.set_password("1234")
    user.save()

    data = {
        "old_password": "1234",
        "password": 'new_pass_1234',
        "password2": "new_pass_1234"
    }

    response = client.patch(URL, data, format='json')

    print(response.data)

    assert response.status_code == 200



@pytest.mark.django_db
def test_forgot_and_reset_password(user):
    # =================================================
    #           FORGOT PASSWORD
    # =================================================
    client = APIClient()
    client.force_authenticate(user)

    user.set_password("1234")
    user.is_active = True
    user.save()

    URL = reverse('forgot-password')

    data = {
        "phone": user.phone
    }

    response = client.post(URL, data, format='json')

    code = cache.get(f"otp:{user.phone}")

    assert response.status_code == 200
    assert code is not None

    # =================================================
    #               RESET PASSWORD
    # =================================================
    URL2 = reverse('reset-password')

    data2 = {
        "phone": user.phone,
        "code": code,
        "password": "changed_pass123",
        "password2": "changed_pass123"
    }

    response = client.post(URL2, data2, format='json')

    assert response.status_code == 200
    assert response.data['message'] == 'Password reset successfully'


