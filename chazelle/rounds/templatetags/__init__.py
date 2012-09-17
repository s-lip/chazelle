from django import template
from django.template.defaultfilters import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def link(value):
    return mark_safe('<a href="%s">%s</a>' % (escape(value.get_absolute_url()), escape(value)))
