from kartify.cart.models import Cart, CartItem
from kartify.cart.utils import get_cart_id


def cart_counter(request):
    if 'admin' in request.path:
        return {}
    cart_count = 0
    for item in CartItem.objects.filter(cart__cart_id=get_cart_id(request), is_active=True):
        cart_count += item.quantity
    return dict(cart_count=cart_count)
