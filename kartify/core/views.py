from django.shortcuts import render

from kartify.store.models import Product


def home(request):
    context = {
        'products': Product.objects.filter(is_available=True)
    }
    return render(request, 'home.html', context=context)
