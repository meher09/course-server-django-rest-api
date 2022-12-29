from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CourseSerializers, MilestoneSerializers, ModuleSerializers, VideoSerializers, CustomRegisterSerializer
from .models import Course, Milestone, Module, Video
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from django.db import IntegrityError


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializers
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        course_slug = self.kwargs.get('course_slug')
        if course_slug:
            queryset = queryset.filter(course__slug=course_slug)
        return queryset


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializers
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        milestone_slug = self.kwargs.get('milestone_slug')
        if milestone_slug:
            queryset = queryset.filter(milestone__slug=milestone_slug)
        return queryset


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        module_slug = self.kwargs.get('module_slug')
        if module_slug:
            queryset = queryset.filter(module__slug=module_slug)
        return queryset


class RegistrationViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = CustomRegisterSerializer(data=request.data, context={
                                              'facebook_id': request.data['facebook_id']})
        if serializer.is_valid():
            try:
                serializer.create(validated_data=serializer.validated_data,
                                  facebook_id=request.data['facebook_id'])
            except IntegrityError:
                return Response({"error": "Email already in use"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
