from django import template

register = template.Library()

@register.filter(name='stringreplace')
def stringreplace(value):
    return value.replace(',', ' ') + " ₽"