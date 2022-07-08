from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Experience
from .forms import ExperienceForm
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
        "object": obj
    }
    return render(request, "experience/detail.html", context=context)

@login_required
def exp_create_view(request):
    form = ExperienceForm(request.POST or None)
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
    return render(request, "experience/create.html", context=context)
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