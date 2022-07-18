from django.urls import path

from .views import (
    praise_list_view, praise_create_view, praise_detail_view
)


urlpatterns = [
    path('', praise_list_view, name='list'),
    path('new/', praise_create_view, name='create'),
    path('<int:id>/', praise_detail_view, name='detail'),
    path('list/<int:month>/', praise_list_view, name='month'),
]