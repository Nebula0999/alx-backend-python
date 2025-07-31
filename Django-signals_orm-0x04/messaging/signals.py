from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.recipient,
            message=instance,
            is_read=False
        )
        print(f"Notification created for {instance.recipient.username} regarding a new message from {instance.sender.username}.")
    else:
        print(f"Message from {instance.sender.username} to {instance.recipient.username} was updated.")
        print(f"Notification not created, message already exists for {instance.recipient.username}.")

