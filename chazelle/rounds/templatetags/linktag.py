from django import template
from django.template.defaultfilters import escape
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

register = template.Library()

@register.filter
def link(value):
    values = value.split(',')
    link_text = values.pop()
    view = ' '.join(values)
    return mark_safe('<a href="%s">%s</a>' % (escape(reverse(view)), escape(link_text)))
