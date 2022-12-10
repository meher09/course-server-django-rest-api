from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'milestones', views.MilestoneViewSet)
router.register(r'modules', views.ModuleViewSet)
router.register(r'videos', views.VideoViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls))
]
