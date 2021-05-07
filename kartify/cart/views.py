from django.shortcuts import render, get_object_or_404, redirect

from kartify.cart.models import Cart, CartItem
from kartify.cart.utils import get_cart_id
from kartify.store.models import Product


def cart(request):
    _cart = Cart.objects.get_or_create(cart_id=get_cart_id(request))[0]
    cart_items = CartItem.objects.filter(cart=_cart, is_active=True)
    total_price = 0
    for item in cart_items:
        total_price += item.sub_total()
    total_price = round(total_price, 2)
    tax = round(0.02 * total_price, 2)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'tax': tax,
        'total': round(total_price + tax, 2)
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    _cart = Cart.objects.get_or_create(cart_id=get_cart_id(request))[0]

    cart_item = CartItem.objects.get_or_create(product=product, cart=_cart)[0]
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:cart')


def remove_from_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    _cart = Cart.objects.get_or_create(cart_id=get_cart_id(request))[0]

    cart_item = CartItem.objects.get_or_create(product=product, cart=_cart)[0]
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:cart')


def remove_cart_item(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    _cart = Cart.objects.get_or_create(cart_id=get_cart_id(request))[0]

    cart_item = CartItem.objects.get_or_create(product=product, cart=_cart)[0]
    cart_item.delete()

    return redirect('cart:cart')

