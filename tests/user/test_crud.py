import pytest

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.authtoken.models import Token

from tests.factories.user import UserFactory
from user.models import UserProfile


@pytest.mark.django_db
def test_create_user():
    url = reverse("user-profile-list")
    data = {'name': 'User Teste', 'email': 'teste_user@gmail.com', 'password': '123456'}

    client = APIClient()
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_list_users():
    user = UserFactory()
    url = reverse("user-profile-list")

    client = APIClient()
    response = client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['name'] == user.name
    assert response.data[0]['email'] == user.email

@pytest.mark.django_db
def test_detail_users():
    user = UserFactory()
    url = reverse("user-profile-detail", args=[user.id])

    client = APIClient()
    response = client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == user.name
    assert response.data['email'] == user.email

@pytest.mark.django_db
def test_update_users():
    user = UserFactory()
    token = Token.objects.create(user=user)
    url = reverse("user-profile-detail", args=[user.id])
    data = {'name': 'User Teste Update'}

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = client.patch(url, data, format='json')

    user_updated = UserProfile.objects.get(id=user.id)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == user_updated.name
    assert response.data['email'] == user_updated.email

@pytest.mark.django_db
def test_delete_user():
    user = UserFactory()
    token = Token.objects.create(user=user)
    url = reverse("user-profile-detail", args=[user.id])

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    # client.force_authenticate(user=user)
    response = client.delete(url, format='json')

    assert response.status_code == status.HTTP_204_NO_CONTENT
