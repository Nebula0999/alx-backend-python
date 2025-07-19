import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'chats.User'
        fields = ['user_id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'role', 'created_at']
        read_only_fields = ['user_id', 'created_at']

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = 'chats.Conversation'
        fields = ['conversation_id', 'participants', 'created_at']
        read_only_fields = ['conversation_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    conversation = serializers.PrimaryKeyRelatedField(queryset='chats.Conversation.objects.all')

    class Meta:
        model = 'chats.Message'
        fields = ['message_id', 'sender', 'message_body', 'sent_at', 'conversation', 'is_read', 'is_deleted']
        read_only_fields = ['message_id', 'sent_at', 'is_read', 'is_deleted']