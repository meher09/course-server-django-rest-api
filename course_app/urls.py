from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet, 'course')
router.register(
    r'courses/(?P<course_slug>[-\w]+)/milestones', MilestoneViewSet, 'milestone')
router.register(
    r'courses/(?P<course_slug>[-\w]+)/milestones/(?P<milestone_slug>[-\w]+)/modules', ModuleViewSet, 'module')
router.register(
    r'courses/(?P<course_slug>[-\w]+)/milestones/(?P<milestone_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/videos', VideoViewSet, 'video')


urlpatterns = [
    path('api/', include(router.urls)),
    path('register/',
         RegistrationViewSet.as_view({'post': 'create'}), name='register'),


]
