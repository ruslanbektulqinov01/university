from django.contrib import admin
from .models import Speciality, Teacher, Subject


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "duration", "duration_unit", "start_date", "is_active")
    search_fields = ("name", "code")
    list_filter = ("duration_unit", "is_active")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "degree", "is_active")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("degree", "is_active")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")
    autocomplete_fields = ("teacher", "speciality")
    