from django import forms

from courses.models import Teacher, Subject


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=100)
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'degree', 'email', 'phone_number')


class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name', 'code', 'description', 'speciality', 'teacher',)
