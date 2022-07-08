from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
