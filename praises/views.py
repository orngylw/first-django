from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from .models import Praise
from .forms import PraiseForm
# Create your views here.

def praise_list_view(request, month=None):
    if month is None:
        praise_list = Praise.objects.values('date__month').annotate(total=Count('id'))
        context = {
            "praises": praise_list,
        }
        
    else:
        praise_list = Praise.objects.filter(date__month=month)
        context = {
            "praises": praise_list,
            "month": month
        }
    return render(request, "praise/list.html", context=context)

def praise_detail_view(request, id):
    obj = Praise.objects.get(id=id)    
    context = {
        "object": obj
    }
    return render(request, "praise/detail.html", context=context)

@login_required
def praise_create_view(request):
    form = PraiseForm(request.POST or None)
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
    return render(request, "praise/create.html", context=context)
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     date = request.POST.get("date")
    #     chord = request.POST.get("chord")
    #     key_up = request.POST.get("key_up")
    #     obj = Praise.objects.create(name=name, date=date, chord=chord, key_up=key_up)
        
    #     created = False
    
    #     if obj is not None:
    #         created = True
    #     context = {
    #         "obj": obj,
    #         "created": created
    #     }
    #     return render(request, "praise/create.html", context=context)
    

