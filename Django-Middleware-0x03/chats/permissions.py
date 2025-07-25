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
            if request.method in permissions.SAFE_METHODS:
                return user in obj.participants.all() and user.is_authenticated
            # Only allow PUT/PATCH/DELETE for participants
            if request.method in ['PUT', 'PATCH', 'DELETE']:
                return user in obj.participants.all() and user.is_authenticated

        # For Message objects
        if hasattr(obj, 'sender'):
            if request.method in permissions.SAFE_METHODS:
                return obj.sender == user or user in obj.conversation.participants.all() and user.is_authenticated
            # Only allow PUT/PATCH/DELETE for the sender
            if request.method in ['PUT', 'PATCH', 'DELETE']:
                return obj.sender == user and user.is_authenticated

        return False