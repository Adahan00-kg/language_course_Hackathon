from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate




class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'username', 'email', 'full_name', 'password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=Teacher.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'email', 'full_name', 'password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=Student.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LoginSerializers(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, data):
        user=authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh=RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError({'detail': 'Недействительный или уже отозванный токен'})



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'status']


class TeacherNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name']


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'status', 'experience', 'about_teacher',
                  'specialization']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'status']


class StudentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['full_name']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title',]


class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'level', 'lesson_id', 'students', 'type', 'submitted_by', 'language_company']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course']

class ExamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'description', 'course', 'passing_score', 'duration', 'questions']

class TeacherReviewListSerializer(serializers.ModelSerializer):
    student = StudentNameSerializer(read_only=True)
    teacher = TeacherNameSerializer(read_only=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')

    class Meta:
        model = TeacherReview
        fields = ['id', 'student', 'teacher','text', 'stars', 'created_date',]

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url' ]


class CourseReviewListSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y  %H:%M')
    class Meta:
        model = CourseReview
        fields = ['student', 'text', 'stars','created_date']


class CourseReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class TeacherReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherReview
        fields = '__all__'


class CourseReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'


class CourseCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCompanyModels
        fields = ['course_company_name','photo']


class CourseLanguageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLanguageModels
        fields = ['connect_company','language_name','level',
                  'price','time_start','time_end']


class CourseLanguageDetailSerializer(serializers.ModelSerializer):
    connect_company = CourseCompanySerializer()
    class Meta:
        model  = CourseLanguageModels
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModels
        fields = '__all__'

