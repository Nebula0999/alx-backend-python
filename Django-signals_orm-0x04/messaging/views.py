from .models import User, Message, MessageHistory, Notification
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect(reverse('home'))  # Redirect to home or login page after deletion
    return render(request, 'delete_user_confirm.html', {'user': user})

def display_thread(message, level=0):
    print("  " * level + f"{message.sender.username}: {message.content}")
    for reply_info in message.get_thread():
        display_thread(reply_info['message'], level + 1)
    messages = Message.objects.filter(parent_message__isnull=True).select_related(
    'sender', 'receiver'
    ).prefetch_related('replies')

def send_message(request):
    if request.method == "POST":
        content = request.POST.get('content')
        receiver_id = request.POST.get('receiver_id')
        receiver = User.objects.get(id=receiver_id)
        Message.objects.create(
            sender=request.user,      # The logged-in user is the sender
            receiver=receiver,        # The recipient user
            content=content
        )
        return redirect('message_list')  # Redirect to the message list after sending

    return render(request, 'send_message.html')

def unread_messages(request):
    if request.user.is_authenticated:
        unread_messages = Message.unread.for_user(request.user)
        return render(request, 'unread_messages.html', {'unread_messages': unread_messages})
    else:
        return redirect('login')