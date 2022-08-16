from django import forms

from .models import Praise


class PraiseForm(forms.ModelForm):
    # def clean(self):
    #     data = self.cleaned_data
    #     return data
    class Meta:
        model = Praise
        labels = {
            'tags': 'Tags (cmd (ctrl) + click for multiple tags)'
        }
        fields = ['name', 'chord', 'key_up', 'instruments', 'date', 'note', 'image', 'file', 'tags']
