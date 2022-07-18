from django import forms


class ProfileChangeForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(),
        required=False,
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(),
        required=False,
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(),
        required=False,
    )
