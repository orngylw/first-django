from django.urls import path

from .views import (
    course_list_view, course_detail_view, course_create_view
)


urlpatterns = [
    path('', course_list_view, name='list'),
    path('new/', course_create_view, name='create'),
    path('<int:id>/', course_detail_view, name='detail'),
]