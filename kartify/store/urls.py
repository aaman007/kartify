from django.urls import path

from kartify.store.views import StoreView, ProductDetailView

app_name = 'store'

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('<slug:slug>/', StoreView.as_view(), name='store_by_category'),
    path('<slug:slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
]
