from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from kartify.core.models import AbstractTimestampModel
from kartify.category.models import Category


class Product(AbstractTimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=200, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=250, unique=True)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/products')
    category = models.ForeignKey(verbose_name=_('Category'), to=Category, on_delete=models.CASCADE)

    price = models.FloatField(verbose_name=_('Price($)'), default=0.0)
    stock = models.PositiveIntegerField(verbose_name=_('Stock'), default=0)
    is_available = models.BooleanField(verbose_name=_('Is Available?'), default=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('store:product_detail', args=[self.category.slug, self.slug])
