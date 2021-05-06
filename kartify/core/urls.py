from django.urls import path

from kartify.core.views import home

app_name = 'core'

urlpatterns = [
    path('', home, name='home')
]
