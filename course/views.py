from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Course
from .forms import CourseForm
from first_django.utils import process_modal_vars


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
        "object": obj,
        "modal": process_modal_vars(
            "Delete Confirmation", "Do you want to delete this content?", "Yes", reverse("courses:delete",
                                                                                         kwargs={"id": id})
        )
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


@login_required
def course_update_view(request, id):
    course_obj = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course_obj.course = form.cleaned_data['course']
            course_obj.subject = form.cleaned_data['subject']
            course_obj.location = form.cleaned_data['location']
            course_obj.instructor = form.cleaned_data['instructor']
            course_obj.grade = form.cleaned_data['grade']
            course_obj.semester = form.cleaned_data['semester']
            course_obj.year = form.cleaned_data['year']
            course_obj.credit = form.cleaned_data['credit']
            course_obj.save()
            return redirect(reverse("courses:list"))

    else:
        form = CourseForm(data={
            'course': course_obj.course,
            'subject': course_obj.subject,
            'location': course_obj.location or None,
            'instructor': course_obj.instructor or None,
            'grade': course_obj.grade,
            'semester': course_obj.semester or None,
            'year': course_obj.year or None,
            'credit': course_obj.credit,
        })
    return render(request, "course/update.html", {"form": form})


@login_required
def course_delete_view(request, id):
    if request.method == "POST":
        course_obj = get_object_or_404(Course, id=id)
        course_obj.delete()
        return redirect(reverse("courses:list"))


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
