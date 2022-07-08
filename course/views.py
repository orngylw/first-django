from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm

# Create your views here.

def course_list_view(request):
    course_queryset = Course.objects.all()
    context = {
        "courses": course_queryset
    }
    return render(request, "course/list.html", context=context)

def course_detail_view(request, id):
    obj = Course.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, "course/detail.html", context=context)

@login_required
def course_create_view(request):
    form = CourseForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        obj = form.save()
        context["obj"] = obj
        created = False
        if obj is not None:
            created = True
        context["created"] = created

    return render(request, "course/create.html", context=context)


    # if request.method == "POST":
    #     course = request.POST.get("course")
    #     subject = request.POST.get("subject")
    #     location = request.POST.get("location")
    #     obj = Course.objects.create(course=course, subject=subject, location=location)
    #     created = False
    #     if obj is not None:
    #         created = True
    #     context = {
    #         "obj": obj,
    #         "created": created
    #     }
    #     return render(request, "course/create.html", context=context)
    
    