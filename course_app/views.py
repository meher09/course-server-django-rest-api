from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

from rest_framework_extensions.mixins import NestedViewSetMixin
# Create your views here.


def home(request):
    context = {}
    return render(request, 'index.html', context)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.filter()


class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all().select_related('course')
    serializer_class = MilestoneSerializers

    def get_queryset(self):
        return Milestone.objects.filter(course=self.kwargs['course_pk'])


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all().select_related('milestone')
    serializer_class = ModuleSerializers

    def get_queryset(self):
        return Module.objects.filter(milestone__course=self.kwargs['course_pk'], milestone=self.kwargs['module_pk'])


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().select_related('milestone')
    serializer_class = VideoSerializers

    def get_queryset(self):
        return Video.objects.filter(module__milestone__course=self.kwargs['course_pk'],
                                    module=self.kwargs['video_pk']
                                    )
