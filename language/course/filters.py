from django_filters import FilterSet
from .models import CourseLanguageModels

class CourseFilter(FilterSet):
    class Meta:
        model = CourseLanguageModels
        fields = {
            'price': ['gt', 'lt'],
            'category': ['exact']
        }