from django import template

register = template.Library()

@register.filter
def last_part(value):
    parts = value.split("\\")
    return parts[-1]