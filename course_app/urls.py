from rest_framework_extensions.routers import (
    ExtendedDefaultRouter as DefaultRouter)
from django.urls import path, include
from . import views

router = DefaultRouter()

# router.register(r'courses', views.CourseViewSet, basename='courses').register(
#     r'milestones', views.MilestoneViewSet, basename='milestones', parents_query_lookups=['course__slug']).register(
#     r'modules', views.ModuleViewSet, basename='modules', parents_query_lookups=['milestone_slug', 'milestone']).register(
#         r'videos', views.VideoViewSet, basename='videos', parents_query_lookups=['module__slug', 'module', 'module_slug'])


router.register(r'courses', views.CourseViewSet)
router.register(r'milestones', views.MilestoneViewSet, basename='milestones')
# router.register(r'modules', views.ModuleViewSet)
# router.register(r'videos', views.VideoViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls))
]
