from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from articles.models import Article
from experience.models import Experience
from course.models import Course
from praises.models import Praise

from .utils import process_modal_vars

import random
import datetime


def home_view(request):
    numb = random.randint(5, 8)
    lucky_number = random.randint(1, 2022)
    welcome=Article.objects.get(id=numb)
    context = {
        "lucky_number": lucky_number,
        "welcome": welcome,
        "modal": process_modal_vars(
            "Modal Title", "Do you want to delete?", "YES",
        )
    }
    return render(request, "home-view.html", context=context)


def form_view(request):
    form_practice = render_to_string("form-view.html")
    return HttpResponse(form_practice)