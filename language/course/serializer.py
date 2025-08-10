from rest_framework import serializers
from .models import *


class CourseCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCompanyModels
        fields = '__all__'

class CourseLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLanguageModels
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModels
        fields = '__all__'


