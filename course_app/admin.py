from django.contrib import admin
from .models import *
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price')


admin.site.register(Course, CourseAdmin)
admin.site.register(Milestone)
admin.site.register(Module)
admin.site.register(Video)
admin.site.register(TeamMember)
admin.site.register(AllowedUser)
