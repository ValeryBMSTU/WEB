from django import template
from asker.models import *

register = template.Library()

@register.inclusion_tag('asker/include/tags.html')
def Hot_tags_users():
    hot_tags = Tag.objects.all()
    hot_users = User.objects.all()
    return {'hot_tags': hot_tags, 'hot_users': hot_users}