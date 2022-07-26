from django import forms

from .models import Experience

class ExperienceForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        # job = data.get("job")
        # qs = Experience.objects.filter(job__icontains=job)
        # if qs.exists():
        #     self.add_error("job", f"{job} is already in use.")
        return data

    class Meta:
        model = Experience
        fields = ['job', 'year', 'desc']