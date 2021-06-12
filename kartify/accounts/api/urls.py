from django.urls import path

from kartify.accounts.api.views import TestAPIView, UsersLCAPIView, UsersRUDAPIView

app_name = 'accounts-api-v1'

urlpatterns = [
    path('test/', TestAPIView.as_view(), name='test-api'),
    path('', UsersLCAPIView.as_view(), name='users-lc-api'),
    path('<int:pk>/', UsersRUDAPIView.as_view(), name='users-rud-api'),
]
