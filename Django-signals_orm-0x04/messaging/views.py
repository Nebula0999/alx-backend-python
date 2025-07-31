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