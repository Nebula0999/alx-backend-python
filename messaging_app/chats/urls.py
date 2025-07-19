from django.urls import path, include
from .views import UserViewSet, ConversationViewSet, MessageViewSet
from rest_framework import routers
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

# Create a router and register our viewsets with it
'''router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]'''

router = NestedDefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'conversations', ConversationViewSet, basename='conversation')

# Create a nested router for messages under conversations
conversations_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
conversations_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(conversations_router.urls)),
]