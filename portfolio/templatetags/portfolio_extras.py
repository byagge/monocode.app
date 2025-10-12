from django import template

register = template.Library()

@register.filter
def split(value, delimiter):
    """Разделяет строку по разделителю"""
    return value.split(delimiter)

@register.filter
def strip(value):
    """Убирает пробелы с начала и конца строки"""
    return value.strip()
