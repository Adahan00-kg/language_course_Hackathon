from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('student/', StudentAPIView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentDetailUpdateDestroyApiView.as_view(), name='student_detail'),
    path('teacher/', TeacherAPIView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/', TeacherRetrieveAPIView.as_view(), name='teacher_detail'),

    path('course_company/',CourseCompanyListAPIView.as_view(),name = 'course_company_list'),
    path('course_language/', CourseLanguageListAPIView.as_view(), name='course_language_list'),
    path('course_language/<int:pk>/', CourseLanguageDetailAPIView.as_view(), name='course_language_detail'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson'),

    path('register/teacher/', TeacherRegisterView.as_view(), name='teacher_register'),
    path('register/student/', StudentRegisterView.as_view(), name='student_register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]