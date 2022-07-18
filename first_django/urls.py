"""first_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .view import home_view
from .view import form_view

from course.views import course_list_view, course_create_view, course_detail_view
from experience.views import exp_list_view, exp_create_view, exp_detail_view
from praises.views import praise_list_view, praise_create_view, praise_detail_view
from accounts.views import login_view, logout_view, register_view, profile_update_view

urlpatterns = [
    path('', home_view, name='home'),
    path('form/', form_view, name='form_view'),
    path('accounts/edit/<int:user_id>', profile_update_view, name='profile_update_view'),
    path('accounts/login/', login_view, name='login_view'),
    path('accounts/logout/', logout_view, name='logout_view'),
    path('accounts/register/', register_view, name='register_view'),
    path('courses/', include(('course.urls', 'course'), namespace='courses')),
    path('exp/', exp_list_view, name='exp_list'),
    path('exp/new/', exp_create_view, name='exp_create'),
    path('exp/<int:id>/', exp_detail_view, name='exp_detail'),
    path('praise/', praise_list_view, name='praise_all'),
    path('praise/new/', praise_create_view, name='praise_create'),
    path('praise/<int:id>/', praise_detail_view, name='praise_detail'),
    path('praise/list/<int:month>/', praise_list_view, name='praise_list'),
    path('admin/', admin.site.urls),
]