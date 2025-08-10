from rest_framework import viewsets, generics, status
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import CourseFilter


class TeacherRegisterView(generics.CreateAPIView):
    serializer_class = TeacherRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentRegisterView(generics.CreateAPIView):
    serializer_class = StudentRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializers

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail: Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user=serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh токен отсутствует."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Вы вышли из системы."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": "Ошибка обработки токена."}, status=status.HTTP_400_BAD_REQUEST)


class StudentAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(id=self.request.user.id)


class StudentDetailUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def get_queryset(self):
        return Student.objects.filter(id=self.request.user.id)


class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['full_name']


class TeacherRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer


class CourseCompanyListAPIView(generics.ListAPIView):
    queryset = CourseCompanyModels.objects.all()
    serializer_class = CourseCompanySerializer


class CourseLanguageListAPIView(generics.ListAPIView):
    queryset = CourseLanguageModels.objects.all()
    serializer_class = CourseLanguageListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['course_name']
    ordering_fields = ['price']


class CourseLanguageDetailAPIView(generics.RetrieveAPIView):
    queryset = CourseLanguageModels.objects.all()
    serializer_class = CourseLanguageDetailSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = LessonModels.objects.all()
    serializer_class = LessonSerializer


class AssignmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AssignmentListSerializer


class AssignmentAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        return Assignment.objects.filter(id=self.request.user.id)


class AssignmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer


class ExamRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer


class ExamCreateAPIView(generics.CreateAPIView):
    serializer_class = ExamCreateSerializer


class ExamAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_queryset(self):
        return Exam.objects.filter(id=self.request.user.id)


class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateCreateAPIView(generics.CreateAPIView):
    serializer_class = CertificateSerializer


class CourseReviewListAPIView(generics.ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer


class CourseRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer
    permission_classes = [CheckEditTeacher]


class CourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckStudentReview]


class TeacherReviewListAPIView(generics.ListAPIView):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewListSerializer


class TeacherReviewDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewCreateSerializer
    permission_classes = [CheckEditTeacher]


class TeacherReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = TeacherReviewCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, CheckStudentReview]