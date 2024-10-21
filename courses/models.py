from django.db import models
from django.utils import timezone


class Speciality(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=4)
    duration_unit = models.CharField(max_length=20, choices=[
        ('weeks', 'Weeks'),
        ('months', 'Months'),
        ('years', 'Years'),
    ], default='years')
    start_date = models.DateField(default=timezone.now)  # Or remove default if not always today
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Speciality'
        ordering = ["name"]  # Default ordering


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    email = models.EmailField()  # Use EmailField for validation
    phone_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'Teacher'


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    speciality = models.ManyToManyField(Speciality)  # Keep ManyToMany here
    teacher = models.ManyToManyField(Teacher)  # Keep ManyToMany here

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Subject'
