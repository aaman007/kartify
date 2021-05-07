from django.views.generic import ListView

from kartify.store.models import Product


class HomeView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'home.html'

    def get_queryset(self):
        return Product.objects.all()[:12]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        })
        return context
