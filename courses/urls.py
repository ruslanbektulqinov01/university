from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='courses'),
    path('speciality/', speciality, name='speciality'),
    path('teacher/', teacher, name='teacher'),
    path('subject/', subject, name='subject'),
    path('subject/<int:pk>/', subject_detials, name='subject-details'),
    path('speciality/create/', speciality_create, name='speciality-create'),
    path('teacher/create/', teacher_create, name='teacher-create'),
    path('subject/create/', subject_create, name='subject-create'),
]