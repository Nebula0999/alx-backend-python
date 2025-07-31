from .models import User, Message, MessageHistory, Notification
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db import models

class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')