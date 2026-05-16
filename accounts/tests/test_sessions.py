import pytest
from rest_framework.test import APIClient
from django.urls import reverse



@pytest.mark.django_db
def test_get_my_sessions(user):
    client = APIClient()
    client.force_authenticate(user)

    user.set_password("1234")
    user.save()

    URL1 = reverse('login')
    data = {
        'phone': user.phone,
        "password": "1234"
    }

    response1 = client.post(URL1, data, format='json')

    print(response1.data)

    assert response1.status_code == 200

    URL = reverse('list-my-sessions')

    response2 = client.get(URL, format='json')
    print(response2.data)

    assert response2.status_code == 200
    assert len(response2.data) == 1
    assert response2.data[0]['user'] == user.id


@pytest.mark.django_db
def test_end_my_session(user):
    client = APIClient()
    client.force_authenticate(user)

    # Login qilib olish kerak birinchi bolip

    user.set_password("1234")
    user.save()

    URL1 = reverse('login')
    data = {
        'phone': user.phone,
        "password": "1234"
    }

    response1 = client.post(URL1, data, format='json')
    print(response1.data)

    assert response1.status_code == 200

    # ==========================================

    # keyin session bormi yoqmi tekshiramiz va jti ni olamiz

    URL2 = reverse('list-my-sessions')

    response2 = client.get(URL2, format='json')
    print(response2.data)

    assert response2.status_code == 200
    assert len(response2.data) == 1
    assert response2.data[0]['user'] == user.id

    # keyin uni jti orqali delete qilamiz

    URL3 = reverse('end-my-session', kwargs={"jti": response2.data[0]['jti']})

    response3 = client.delete(URL3, format='json')
    print(response3.data)

    assert response3.status_code == 200

