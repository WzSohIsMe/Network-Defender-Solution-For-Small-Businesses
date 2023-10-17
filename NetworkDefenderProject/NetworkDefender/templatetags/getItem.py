from django import template
register = template.Library()



@register.filter(name='get_item')
def get_item(d, key_name):
    try:
        value = d[key_name]
    except KeyError:
        from django.conf import settings

        value = settings.TEMPLATE_STRING_IF_INVALID

    return value

register.filter('get_item',get_item)