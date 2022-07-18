from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .forms import ProfileChangeForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "accounts/login.html", context)


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect(reverse('accounts:login'))
    context = {"form": form}
    return render(request, "accounts/register.html", context)


@login_required
def profile_update_view(request):
    user_obj = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = ProfileChangeForm(request.POST)
        if form.is_valid():
            user_obj.first_name = form.cleaned_data['first_name']
            user_obj.last_name = form.cleaned_data['last_name']
            user_obj.email = form.cleaned_data['email']
            user_obj.save()
            return redirect('/')
    else:
        form = ProfileChangeForm(data={
            'first_name': user_obj.first_name or None,
            'last_name': user_obj.last_name or None,
            'email': user_obj.email or None,
        })

    return render(request, "accounts/update.html", {"form": form})


@login_required()
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect(reverse('accounts:login'))
    return render(request, "accounts/logout.html", {})
# def login_view(request):
#     if request.user.is_authenticated:
#         return render(request, "accounts/loggedin.html", context={})
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             error = "Invalid username or password"
#             context = {
#                 "error": error,
#             }
#             return render(request, "accounts/login.html", context=context)
#     return render(request, "accounts/login.html", context={})
#
#
# def logout_view(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect("/")
#     return render(request, "accounts/logout.html", context={})
#
#
# def register_view(request):
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.save()
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password1"]
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(f'/accounts/edit/{user_obj.id}')
#     context = {"form": form}
#     return render(request, "accounts/register.html", context)
#
#
# @login_required
# def profile_update_view(request):
#     user_obj = get_object_or_404(User, id=request.user.id)
#     form = ProfileChangeForm(request.POST or None, instance=user_obj)
#
#     if form.is_valid():
#         user_obj = form.save()
#         return redirect(f'/accounts/edit/{user_obj.id}')
#
#     context = {"form": form}
#     return render(request, "accounts/update.html", context)
