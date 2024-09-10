from django import template
from subekashi.constants.view import DEFAULT_DESCRIPTION

register = template.Library()

@register.simple_tag
def get_description(description):
    return description if description else DEFAULT_DESCRIPTION
