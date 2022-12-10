from django.contrib import admin
from django.urls import path, include
from course_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course_app.urls')),


]
