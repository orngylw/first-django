from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse


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


@login_required
def praise_update_view(request, id):
    praise_obj = get_object_or_404(Praise, id=id)

    if request.method == 'POST':
        form = PraiseForm(request.POST)
        if form.is_valid():
            praise_obj.name = form.cleaned_data['name']
            praise_obj.instruments = form.cleaned_data['instruments']
            praise_obj.chord = form.cleaned_data['chord']
            praise_obj.key_up = form.cleaned_data['key_up']
            praise_obj.date = form.cleaned_data['date']
            praise_obj.note = form.cleaned_data['note']
            praise_obj.save()
            return redirect(reverse("praises:list"))

    else:
        form = PraiseForm(data={
            'name': praise_obj.name,
            'instruments': praise_obj.instruments or None,
            'chord': praise_obj.chord or None,
            'key_up': praise_obj.key_up,
            'date': praise_obj.date,
            'note': praise_obj.note or None,
        })
    return render(request, "praise/update.html", {"form": form})




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
    

