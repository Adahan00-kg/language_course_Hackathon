from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS_CHOICES = (
    ('student', 'student'),
    ('teacher', 'teacher'),
)

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.full_name} {self.email}'


class Student(UserProfile):
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='student')

    class Meta:
        verbose_name_plural = "Student"


class Teacher(UserProfile):
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='teacher')
    experience = models.CharField(max_length=64)
    about_teacher = models.TextField()
    specialization = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Teacher"

    def __str__(self):
        return f'{self.full_name} -- {self.status}'



