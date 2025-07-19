from django.urls import path, include
from .views import UserViewSet, ConversationViewSet, MessageViewSet
from rest_framework import routers

# Create a router and register our viewsets with it
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]