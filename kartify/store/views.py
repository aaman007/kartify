from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from kartify.cart.models import CartItem
from kartify.cart.utils import get_cart_id
from kartify.category.models import Category
from kartify.store.models import Product


class StoreView(ListView):
    model = Product
    paginate_by = 6
    context_object_name = 'products'
    template_name = 'store/store.html'

    def get_category(self):
        try:
            return Category.objects.get(slug=self.kwargs.get('slug'))
        except Category.DoesNotExist:
            return None

    def get_queryset(self):
        category = self.get_category()
        search_term = self.request.GET.get('search')
        q_exp = Q(is_available=True)
        if category:
            q_exp &= Q(category=category)
        if search_term:
            q_exp &= Q(name__icontains=search_term) | Q(description__icontains=search_term)
        return Product.objects.filter(q_exp).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'category': self.get_category(),
            'product_count': self.get_queryset().count()
        })
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store/product_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Product, slug=self.kwargs.get('product_slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        in_cart = CartItem.objects.filter(
            cart__cart_id=get_cart_id(self.request), product__slug=self.kwargs.get('product_slug')
        ).exists()
        context.update({
            'in_cart': in_cart
        })
        return context
