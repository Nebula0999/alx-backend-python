from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=128, null=False)
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False, db_index=True)
    participants = models.ManyToManyField('User', related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Conversation {self.conversation_id} with {self.participants.count()} participants"
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False, db_index=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    is_read = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.sender.email} in conversation {self.conversation.id}"
    
class Property(models.Model):
    property_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False, db_index=True)
    # ...other fields...

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False, db_index=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, db_index=True)
    # ...other fields...

class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, db_index=True)
    # ...other fields...
