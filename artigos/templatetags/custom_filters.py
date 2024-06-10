# templatetags/custom_filters.py
from django import template
from artigos.models import Rating

register = template.Library()

@register.filter
def get_rating(comment):
    rating = Rating.objects.filter(comment=comment).first()
    return rating

@register.filter
def get_range(value):
    return range(value)
