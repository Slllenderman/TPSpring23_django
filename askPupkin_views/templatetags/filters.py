from django import template
from django.contrib.contenttypes.models import ContentType
from askPupkin_models.models import *
register = template.Library()

@register.filter
def convert_rating(rating):
    if rating > 4 and rating < 21:
        return str(rating) + " оценок"
    if rating % 10 == 1:
        return str(rating) + " оценка"
    if rating % 10 >= 2 and rating % 10 <= 4:
        return str(rating) + " оценки"
    else:
        return str(rating) + " оценок"

@register.filter
def choice_format(question, isCard):
    SMALL_BREACKPOINT = 170
    BIG_BREACKPOINT = 600
    title_weight = 1.5
    content_weight = 1.1
    symb_summary = 0
    if isCard:
        symb_summary = len(question.title) * title_weight + len(question.description) * content_weight
        if symb_summary < SMALL_BREACKPOINT:
            return 'cards/small_question.html'
    else:
        symb_summary = len(question.title) * title_weight + len(question.content) * content_weight
        if symb_summary > BIG_BREACKPOINT:
            return 'cards/big_question.html'
    return 'cards/question.html'
