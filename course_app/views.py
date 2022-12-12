from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework_extensions.mixins import NestedViewSetMixin
# Create your views here.


def home(request):
    context = {}
    return render(request, 'index.html', context)


class CourseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'slug'


class MilestoneViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
    lookup_field = 'slug'


class ModuleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    lookup_field = 'slug'


class VideoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'
