from django import template
from askPupkin_models.models import *
import re

register = template.Library()

def add_param(path, parameter, key):
    if "?" not in path:
        path += "?"
    if parameter not in path:
        path += f"&{key}={parameter}"
    return path

def del_param(path, parameter, key):
    return path.replace(f"{key}={parameter}", "").replace("&&", "&").replace("?&", "?")

@register.filter
def add_orderby(path, parameter):
    path = re.sub("page=\d+", "", path)
    return add_param(path, parameter, "order_by")


@register.filter
def del_orderby(path, parameter):
    path = re.sub("page=\d+", "", path)
    return del_param(path, parameter, "order_by")

@register.filter
def add_tag(path, parameter):
    path = re.sub("page=\d+", "", path)
    return add_param(path, parameter, "tag")

@register.filter
def del_tag(path, parameter):
    path = re.sub("page=\d+", "", path)
    return del_param(path, parameter, "tag")

@register.filter
def add_page(path, parameter):
    path = re.sub("page=\d+", "", path)
    return add_param(path, parameter, "page").replace("&&", "&").replace("?&", "?")