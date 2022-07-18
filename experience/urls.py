from django.urls import path

from .views import (
    exp_list_view, exp_create_view, exp_detail_view
)


urlpatterns = [
    path('', exp_list_view, name='list'),
    path('new/', exp_create_view, name='create'),
    path('<int:id>/', exp_detail_view, name='detail'),
]