from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import *
register = template.Library()

@register.filter
def convert_rating(value):
    rating = value
    if rating > 4 and rating < 21:
        return str(rating) + " оценок"
    if rating % 10 == 1:
        return str(rating) + " оценка"
    if rating % 10 >= 2 and rating % 10 <= 4:
        return str(rating) + " оценки"
    else:
        return str(rating) + " оценок"
    