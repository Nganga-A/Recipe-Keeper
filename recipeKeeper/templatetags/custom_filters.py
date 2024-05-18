from django import template

register = template.Library()

@register.filter
def split_instructions(cooking_instructions):
    return cooking_instructions.split(".")