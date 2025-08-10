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

    def __str__(self):
        return f'{self.full_name} {self.status}'


class Teacher(UserProfile):
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='teacher')
    experience = models.CharField(max_length=64)
    about_teacher = models.TextField()
    specialization = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Teacher"

    def __str__(self):
        return f'{self.full_name} {self.status}'

class CourseCompanyModels(models.Model):
    course_company_name = models.CharField(max_length=128,unique=True)
    created_date = models.DateField(auto_created=True)
    description = models.TextField(null=True,blank=True)
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='course')
    photo = models.ImageField(upload_to='profile_photo')


class CourseLanguageModels(models.Model):
    language_name = models.CharField(max_length=50)
    created_date = models.DateField(auto_created=True)
    description = models.TextField(null=True,blank=True)
    level = models.CharField(max_length=25,choices=LEVEL_CHOICES)
    teacher = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='language')
    time = models.TimeField(null=True,blank=True)
    price = models.PositiveIntegerField()


class LessonModels(models.Model):
    lesson_name = models.CharField(max_length=150)
    created_time = models.DateTimeField(auto_created=True)
    description = models.TextField(null=True,blank=True)
    lesson_material = models.FileField(upload_to='lesson_material')
    teacher = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='lesson')


class Assignment(models.Model):
    TYPE_LESSON_CHOICES = (
        ('test', 'test'),
        ('text', 'text'),
        ('file', 'file'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    level = models.CharField(choices=LEVEL_CHOICES, max_length=100)
    lesson_id = models.ForeignKey(CourseLanguageModels, on_delete=models.CASCADE, related_name='lesson_assignment')
    students = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(choices=TYPE_LESSON_CHOICES, max_length=100)
    submitted_by = models.TextField()
    language_company = models.ForeignKey(CourseCompanyModels, on_delete=models.CASCADE, related_name='owner_assignment')

    def __str__(self):
        return f'{self.title}'


class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(CourseLanguageModels, on_delete=models.CASCADE, related_name='course_exam')
    passing_score = models.PositiveSmallIntegerField(null=True, blank=True)
    duration = models.DurationField()
    questions = models.CharField(max_length=526)

    def __str__(self):
        return f'{self.title}'

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='certificate_student')
    course = models.ForeignKey(CourseLanguageModels, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return f'{self.student} -- {self.course}'


class CourseReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseLanguageModels, on_delete=models.CASCADE, related_name='reviews_course')
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='рейтинг')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, - {self.stars}'


class TeacherReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='reviews_teacher')
    text = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='рейтинг')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student}, - {self.stars}'


