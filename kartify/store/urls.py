from django.urls import path

from kartify.store.views import store, product_detail

app_name = 'store'

urlpatterns = [
    path('', store, name='store'),
    path('<slug:slug>/', store, name='store_by_category'),
    path('<slug:slug>/<slug:product_slug>/', product_detail, name='product_detail'),
]
