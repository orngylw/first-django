from django.urls import path

from .views import (
    praise_list_view, praise_create_view, praise_detail_view, praise_update_view, praise_delete_view
)


urlpatterns = [
    path('', praise_list_view, name='list'),
    path('new/', praise_create_view, name='create'),
    path('edit/<int:id>/', praise_update_view, name='edit'),
    path('delete/<int:id>/', praise_delete_view, name='delete'),
    path('<int:id>/', praise_detail_view, name='detail'),
    path('list/<int:month>/', praise_list_view, name='month'),

]