from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer

class UserViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass',)
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpass')
        self.client.login(username='admin', password='adminpass')

        self.url = reverse('user-list', kwargs={'username': self.user.username})

    def test_create_user(self):
        response = self.user.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], 'testuser')