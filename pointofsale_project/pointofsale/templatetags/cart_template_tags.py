from django import template
from pointofsale.models import Purchase

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Purchase.objects.filter(user=user, purchased=False)
        if qs.exists():
            return qs[0].product.count()
    return 0
