from random import choice

from django.contrib.auth.models import AbstractUser
from django.db import models


LEVEL_CHOICES = (
    ('A0','A0'),
    ('A1','A1'),
    ('A2','A2'),
    ('A1-A2','A1-A2'),
    ('B1','B1'),
    ('B2','B2'),
    ('B1-B2', 'B1-B2'),
    ('C1','C1')
)

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
        return f'{self.first_name} {self.last_name} -- {self.status}'

class CourseCompanyModels(models.Model):
    course_company_name = models.CharField(max_length=128,unique=True)
    created_date = models.DateField(auto_created=True)
    description = models.TextField(null=True,blank=True)
    owner = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='course')
    photo = models.ImageField(upload_to='profile_photo')


    def __str__(self):
        return f'{self.course_company_name} - {self.owner}'


class CourseLanguageModels(models.Model):
    connect_company = models.ForeignKey(CourseCompanyModels,on_delete=models.CASCADE,related_name='language')
    language_name = models.CharField(max_length=50)
    created_date = models.DateField(auto_created=True)
    description = models.TextField(null=True,blank=True)
    level = models.CharField(max_length=25,choices=LEVEL_CHOICES)
    teacher = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='language')
    time_start = models.TimeField(null=True,blank=True)
    time_end  =models.TimeField(null=True,blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.language_name} {self.level}'


class LessonModels(models.Model):
    lesson_name = models.CharField(max_length=150)
    created_time = models.DateTimeField(auto_created=True)
    description = models.TextField(null=True,blank=True)
    lesson_material = models.FileField(upload_to='lesson_material')
    connect_course = models.ForeignKey(CourseLanguageModels,on_delete=models.CASCADE,related_name='lesson')
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='lesson')
    def __str__(self):
        return f'{self.lesson_name} {self.teacher}'
