from django import template
register = template.Library()


@register.filter
def multiply(unit_price, quantity, *args, **kwargs):
    return unit_price * quantity
