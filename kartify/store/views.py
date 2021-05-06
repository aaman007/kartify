from django.shortcuts import render, get_object_or_404

from kartify.category.models import Category
from kartify.store.models import Product


def store(request, slug=None):
    category = None
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(is_available=True, category=category)
    else:
        products = Product.objects.filter(is_available=True)
    product_count = products.count()
    context = {
        'category': category,
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, slug, product_slug):
    context = {
        'product': get_object_or_404(Product, slug=product_slug)
    }
    return render(request, 'store/product_detail.html', context=context)
