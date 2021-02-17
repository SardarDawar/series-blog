from django import template
# from django.shortcuts import get_object_or_404
# from ..models import Episode 

register = template.Library()


@register.filter(name='is_in_like')
def is_in_like(episode, like):
    keys = like.keys()
    for id in keys:
        if int(id) == episode.id:
            likeCount = like.get(id)
            if likeCount >= 1:
                return True
    return False

@register.filter(name='how_many_in_cart')
def how_many_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            cartGet = cart.get(id)
            return cartGet
    return 0