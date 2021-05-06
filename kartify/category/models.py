from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from kartify.core.models import AbstractTimestampModel


class Category(AbstractTimestampModel):
    title = models.CharField(verbose_name=_('Title'), max_length=50, unique=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    description = models.CharField(verbose_name=_('Description'), max_length=255, blank=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='images/category', blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('store:store_by_category', args=[self.slug])
