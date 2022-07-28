from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Experience
from .forms import ExperienceForm
from first_django.utils import process_modal_vars, process_form_vars
# Create your views here.


def exp_list_view(request):
    exp_list = Experience.objects.all()
    context = {
        "experiences": exp_list
    }
    return render(request, "experience/list.html", context=context)


def exp_detail_view(request, id):
    obj = Experience.objects.get(id=id)
    context = {
        "object": obj,
        "modal": process_modal_vars(
            "Delete Confirmation", "Do you want to delete this content?", "Yes", reverse("experience:delete",
                                                                                         kwargs={"id": id})
        )
    }
    return render(request, "experience/detail.html", context=context)


@login_required
def exp_create_view(request):
    form = ExperienceForm(request.POST or None)
    context = {
        "form": form,
        "generic_form": process_form_vars("Create", reverse("experience:list"))
    }

    if form.is_valid():
        obj = form.save()
        context["obj"] = obj
        created = False
        if obj is not None:
            created = True
        context["created"] = created
    return render(request, "experience/create.html", context=context)


@login_required
def exp_update_view(request, id):
    exp_obj = get_object_or_404(Experience, id=id)
    context= {
        "generic_form": process_form_vars(label="Update", back_url=reverse("experience:list"),
                                          actio_url=reverse("experience:edit", kwargs={"id": id}))
    }

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            exp_obj.job = form.cleaned_data['job']
            exp_obj.year = form.cleaned_data['year']
            exp_obj.desc = form.cleaned_data['desc']
            exp_obj.save()
            return redirect(reverse("experience:list"))

    else:
        form = ExperienceForm(data={
            'job': exp_obj.job,
            'year': exp_obj.year,
            'desc': exp_obj.desc,
        })
        context["form"] = form
    return render(request, "experience/update.html", context=context)


@login_required
def exp_delete_view(request, id):
    if request.method == "POST":
        exp_obj = get_object_or_404(Experience, id=id)
        exp_obj.delete()
        return redirect(reverse("experience:list"))

    # if request.method == "POST":
    #     job = request.POST.get("job")
    #     desc = request.POST.get("desc")
    #     year = request.POST.get("year")
    #     obj = Experience.objects.create(job=job, desc=desc, year=year)
        
    #     created = False
    
    #     if obj is not None:
    #         created = True
    #     context = {
    #         "obj": obj,
    #         "created": created
    #     }
    #     return render(request, "experience/create.html", context=context)
    
    # return render(request, "experience/create.html", context={})