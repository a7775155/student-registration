
# students/admin.py

from django.contrib import admin
from .models import Student, Course

class CourseAdmin(admin.ModelAdmin):
    # The 'schedule' field has been removed as it does not exist in the Course model.
    list_display = ('course_code', 'course_name', 'instructor', 'credits')
admin.site.register(Student)
admin.site.register(Course, CourseAdmin) # Register Course with our new admin class
