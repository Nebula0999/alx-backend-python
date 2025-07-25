from django.contrib import admin
from .models import User, Conversation, Message, Property, Booking, Payment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'role', 'created_at')
    search_fields = ('username', 'email')
    list_filter = ('role',)

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('conversation_id', 'created_at')
    search_fields = ('participants__username',)
    filter_horizontal = ('participants',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'sender', 'conversation', 'sent_at', 'is_read', 'is_deleted')
    search_fields = ('sender__username', 'conversation__conversation_id')
    list_filter = ('is_read', 'is_deleted')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'property')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'booking')
# Register your models here.
