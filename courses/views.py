from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SpecialityForm, TeacherModelForm, SubjectModelForm
from .models import Speciality, Teacher, Subject


def index(request):
    name = request.GET.get('name', 'Django')
    return HttpResponse("Hello " + name + "!")


def speciality(request):
    spec = Speciality.objects.all()
    context = {'spec': spec}
    return render(request, 'home.html', context)


def teacher(request):
    search = request.GET.get('search')
    if search:
        teachers = Teacher.objects.filter(name__icontains=search)
    else:
        teachers = Teacher.objects.all()

    context = {'teachers': teachers}
    return render(request, 'teacher.html', context)


def subject(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subject.html', context)


def subject_detials(request, pk):
    subject = Subject.objects.get(pk=pk)
    context = {'subject': subject}
    return render(request, 'subject_details.html', context)


def speciality_create(request):
    if request.method == 'GET':
        form = SpecialityForm()
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Speciality.objects.create(**data)
        return redirect('speciality')

    context = {'form': form}
    return render(request, 'speciality_create.html', context)


def teacher_create(request):
    if request.method == 'GET':
        form = TeacherModelForm()
    else:
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Teacher.objects.create(**data)
        return redirect('teacher')
    context = {'form': form}
    return render(request, 'teacher_create.html', context)


def subject_create(request):
    if request.method == 'GET':
        form = SubjectModelForm()
    else:
        form = SubjectModelForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            data.speciality.set(form.cleaned_data['speciality'])
            data.teacher.set(form.cleaned_data['teacher'])
            return redirect('subject')
    context = {'form': form}
    return render(request, 'subject_create.html', context)




