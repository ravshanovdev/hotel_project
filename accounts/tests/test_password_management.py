import pytest
from rest_framework.test import APIClient
from django.urls import reverse


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



