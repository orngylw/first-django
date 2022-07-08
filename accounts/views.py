from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


# Create your views here.
from accounts.forms import ProfileChangeForm


def login_view(request):
    if request.user.is_authenticated:
        return render(request, "accounts/loggedin.html", context={})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            error = "Invalid username or password"
            context = {
                "error": error,
            }
            return render(request, "accounts/login.html", context=context)
    return render(request, "accounts/login.html", context={})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, "accounts/logout.html", context={})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/accounts/edit/{user_obj.id}')
    context = {"form": form}
    return render(request, "accounts/register.html", context)


@login_required
def profile_update_view(request, user_id):
    user_obj = get_object_or_404(User, id=user_id)
    form = ProfileChangeForm(request.POST or None, instance=user_obj)
    if form.is_valid():
        user_obj = form.save()
        return redirect(f'/accounts/edit/{user_obj.id}')
    context = {"form": form}
    return render(request, "accounts/update.html", context)



    # if request.user.is_authenticated:
    #     logout(request)
    #     return render(request, "accounts/logout.html", context={})
    # else:
    #     error = "You're not signed in. Please sign in first"
    #     context = {
    #         "error": error,
    #     }
    # return render(request, "accounts/logout.html", context=context)
