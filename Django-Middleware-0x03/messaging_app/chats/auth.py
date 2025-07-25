from .models import User, Conversation, Message, Property, Booking, Payment
from django.contrib import admin
from rest_framework import authentication, permissions


class IsAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to perform write operations.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated