from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import User, Message, MessageHistory, Notification

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            MessageHistory.objects.create(
                message=instance,
                old_content=old_message.content
            )
            instance.edited = True

@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            is_read=False
        )
        print(f"Notification created for {instance.receiver.username} regarding a new message from {instance.sender.username}.")
    else:
        print(f"Message from {instance.sender.username} to {instance.receiver.username} was updated.")
        print(f"Notification not created, message already exists for {instance.receiver.username}.")
        
@receiver(post_delete, sender=User)
def cleanup_user_related_data(sender, instance, **kwargs):
    # Delete messages sent or received by the user
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    # Delete notifications for the user
    Notification.objects.filter(user=instance).delete()
    # Delete message histories for messages sent or received by the user
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()

for history in message.history.all():
    print(f"Edited at {history.edited_at}: {history.old_content}")

