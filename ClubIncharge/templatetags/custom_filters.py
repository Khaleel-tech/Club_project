from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if not dictionary:
        return ""
    return dictionary.get(str(key), "")

@register.filter
def filter_active(queryset):
    if not queryset:
        return []
    now = timezone.now()
    return [item for item in queryset if hasattr(item, 'start_date') and hasattr(item, 'end_date') and item.start_date <= now <= item.end_date]

@register.filter
def filter_upcoming(queryset):
    if not queryset:
        return []
    now = timezone.now()
    return [item for item in queryset if hasattr(item, 'start_date') and item.start_date > now]

@register.filter
def length(queryset):
    if not queryset:
        return 0
    return len(queryset) 