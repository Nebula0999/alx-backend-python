from .models import User, Conversation, Message
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def validate_email(self, value):
        if "spam" in value:
            raise serializers.ValidationError("Invalid email address.")
        return value

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at']
        read_only_fields = ['conversation_id', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    conversation = serializers.PrimaryKeyRelatedField(queryset='chats.Conversation.objects.all')

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at', 'conversation', 'is_read', 'is_deleted']
        read_only_fields = ['message_id', 'sent_at', 'is_read', 'is_deleted']

class CustomUserSerializer(serializers.ModelSerializer):
    custom_field = serializers.CharField(required=False, max_length=100)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'custom_field']