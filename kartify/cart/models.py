from django.db import models
from django.utils.translation import gettext_lazy as _

from kartify.store.models import Product


class Cart(models.Model):
    cart_id = models.CharField(verbose_name=_('Cart Id'), max_length=200)
    date_added = models.DateField(verbose_name=_('Date Added'), auto_now_add=True)

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    cart = models.ForeignKey(verbose_name=_('Cart'), to='Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name=_('Product'), to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'), default=0)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')

    def __str__(self):
        return self.product.name

    def sub_total(self):
        return round(self.product.price * self.quantity, 2)
