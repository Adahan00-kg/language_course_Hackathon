from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(UserProfile)
admin.site.register(CourseCompanyModels)
admin.site.register(CourseLanguageModels)
admin.site.register(LessonModels)
admin.site.register(Assignment)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(CourseReview)
admin.site.register(TeacherReview)