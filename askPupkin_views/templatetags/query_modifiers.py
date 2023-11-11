from django import template
from django.contrib.contenttypes.models import ContentType
from askPupkin_models.models import *

def add_param(path, parameter, key):
    if "?" not in path:
        path += "?"
    if parameter not in path:
        path += f"{key}={parameter}&"
    return path

def del_param(path, parameter, key):
    return path.replace(f"{key}={parameter}", "").replace("&&", "&").replace("?&", "?")    

register = template.Library()

@register.filter
def add_orderby(path, parameter):
    return add_param(path, parameter, "order_by")


@register.filter
def del_orderby(path, parameter):
    return del_param(path, parameter, "order_by")

@register.filter
def add_tag(path, parameter):
    return add_param(path, parameter, "tag")

@register.filter
def del_tag(path, parameter):
    return del_param(path, parameter, "tag")