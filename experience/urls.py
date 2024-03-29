from django.urls import path

from .views import (
    exp_list_view, exp_create_view, exp_detail_view, exp_update_view, exp_delete_view
)


urlpatterns = [
    path('', exp_list_view, name='list'),
    path('new/', exp_create_view, name='create'),
    path('edit/<int:id>/', exp_update_view, name='edit'),
    path('delete/<int:id>/', exp_delete_view, name='delete'),
    path('<int:id>/', exp_detail_view, name='detail'),
]