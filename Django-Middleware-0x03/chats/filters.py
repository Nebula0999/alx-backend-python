from django_filters import rest_framework as filters
from rest_framework.response import Response
from .models import Message

class MessageFilter(filters.FilterSet):
    """
    Custom filter to filter messages by conversation and sender.
    """
    conversation = filters.CharFilter(field_name='conversation__id', lookup_expr='exact')
    sender = filters.CharFilter(field_name='sender__id', lookup_expr='exact')
    sent_after = filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    sent_before = filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['conversation', 'sender', 'sent_after', 'sent_before']

    def filter_queryset(self, request, queryset, view):
        queryset = super().filter_queryset(request, queryset, view)
        return queryset