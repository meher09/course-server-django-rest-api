from django.urls import path, include
from .views import *
from rest_framework_nested import routers
from rest_framework import routers as r

router = routers.SimpleRouter()
router.register(r'courses', CourseViewSet, basename='courses')


milestone_router = routers.NestedSimpleRouter(
    router, r'courses', lookup='course')

milestone_router.register(
    r'milestones', MilestoneViewSet, basename='course-milestone')


module_router = routers.NestedSimpleRouter(
    milestone_router, r'milestones', lookup='module')

module_router.register(r'modules', ModuleViewSet, basename='modules')


video_router = routers.NestedSimpleRouter(
    module_router, r'modules', lookup='video')

video_router.register(r'videos', VideoViewSet, basename='videos')


app_name = 'course_app'

urlpatterns = [
    path('', home, name='home'),
    path(r'api/', include(router.urls)),
    path(r'api/', include(milestone_router.urls)),
    path(r'api/', include(module_router.urls)),
    path(r'api/', include(video_router.urls)),


]
