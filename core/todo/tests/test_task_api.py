from django.utils import timezone
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email = "mhm@admin.com", password="a/@1234567")
    return user

@pytest.mark.django_db
class TestTaskApi:
    
    def test_create_task_response_201_status(self, common_user, api_client):
        # test for creating new task when user was login
        url = reverse('api-viewset:tasks-list')
        data = {
            'title':'test from pytest',
            'complete' : True,
        }
        api_client.force_authenticate(user=common_user) # for login user
        response = api_client.post(url, data) 
        assert response.status_code == 201 #!reminder::401 means it's not authenticated , 403 means Forbbiden that mean that user is not allowed , 201 means post created successfully
    
    def test_get_task_response_200_status(self, api_client, common_user):
        # test for getting task lists when the user is login
        url = reverse('api-viewset:tasks-list')
        api_client.force_authenticate(user=common_user)
        response = api_client.get(url)
        assert response.status_code == 201
    
    
    def test_create_task_invalid_data_response_400_status(self, api_client, common_user):
        # test for create new task with wrong data type
        url = reverse("api-viewset:tasks-list")
        data = {
            'title':'test from pytest',
            'complete' : 'string',
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 400 # 400 means Bad Request