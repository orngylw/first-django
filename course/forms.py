from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    def clean(self):
        data = self.cleaned_data
        # Create 할 때는 중복되면 안되지만 Edit 에서도 중복된다고 뜨면서 Update가 안됨
        # course = data.get("course")
        # subject = data.get("subject")
        # qs = Course.objects.filter(course__icontains=course)
        # if qs.exists():
        #     self.add_error("course", f"{course} is already in use.")
        # qs = Course.objects.filter(subject__icontains=subject)
        # if qs.exists():
        #     self.add_error("subject", f"{subject} is already in use")
        return data

    class Meta:
        model = Course
        fields = ['course', 'subject', 'location', 'instructor', 'credit', 'grade', 'semester', 'year']