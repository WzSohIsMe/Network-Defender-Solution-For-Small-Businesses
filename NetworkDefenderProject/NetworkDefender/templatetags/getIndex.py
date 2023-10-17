from django import template
register = template.Library()



@register.filter(name='get_index')
def get_index(lst, i):
    return lst[i]

register.filter('get_index',get_index)