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

    path('assignment/create/', AssignmentCreateAPIView.as_view(), name='assignment_create'),
    path('assignment_list/', AssignmentAPIView.as_view(), name='assignment_list'),
    path('assignment_list/<int:pk>/', AssignmentRetrieveUpdateDestroyAPIView.as_view(), name='assignment_list_edit'),
    path('exam/<int:pk>', ExamRetrieveAPIView.as_view(), name='exam_detail'),
    path('exam/create/', ExamCreateAPIView.as_view(), name='exam_create'),
    path('exam_list/', ExamAPIView.as_view(), name='exam_list'),
    path('certificates/', CertificateListAPIView.as_view(), name='certificate_list'),
    path('certificates/create/', CertificateCreateAPIView.as_view(), name='certificates_create'),
    path('reviews/', CourseReviewListAPIView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', CourseRetrieveDestroyAPIView.as_view(), name='review_detail'),
    path('review/create/', CourseReviewCreateAPIView.as_view(), name='review_create'),
    path('teacher_reviews/', TeacherReviewListAPIView.as_view(), name='teacher_review_list'),
    path('teacher_reviews/<int:pk>/', TeacherReviewDetailUpdateDestroyAPIView.as_view(), name='teacher_review_detail'),
    path('teacher_reviews/create/', TeacherReviewCreateAPIView.as_view(), name='teacher_review_create'),
    path('register/teacher/', TeacherRegisterView.as_view(), name='teacher_register'),
    path('register/student/', StudentRegisterView.as_view(), name='student_register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]