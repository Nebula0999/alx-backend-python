from .models import User, Conversation, Message, Property, Booking, Payment
from rest_framework import authentication
from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation
    or sender/recipient of a message to access them.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # For Conversation objects
        if hasattr(obj, 'participants'):
            return user in obj.participants.all()

        # For Message objects
        if hasattr(obj, 'sender'):
            return obj.sender == user or user in obj.conversation.participants.all()

        return False