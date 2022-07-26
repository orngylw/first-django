from django.urls import path

from .views import (
    course_list_view, course_detail_view, course_create_view, course_update_view, course_delete_view
)


urlpatterns = [
    path('', course_list_view, name='list'),
    path('new/', course_create_view, name='create'),
    path('edit/<int:id>/', course_update_view, name='edit'),
    path('delete/<int:id>/', course_delete_view, name='delete'),
    path('<int:id>/', course_detail_view, name='detail'),
]