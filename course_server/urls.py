from django.contrib import admin
from django.urls import path, include
from course_app import views


urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('', include('course_app.urls')),


]
