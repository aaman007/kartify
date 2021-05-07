from django.urls import path

from kartify.cart.views import cart, add_to_cart, remove_from_cart, remove_cart_item

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('add-to-cart/<slug:product_slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug:product_slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove-cart-item/<slug:product_slug>/', remove_cart_item, name='remove_cart_item'),
]
