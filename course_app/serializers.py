from rest_framework.serializers import ModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

from .models import *


class CourseSerializers(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class ModuleSerializers(ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class MilestoneSerializers(ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'



