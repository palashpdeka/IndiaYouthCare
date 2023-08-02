from django.contrib import admin
from courses.models import course_details

class course_admin(admin.ModelAdmin):
    list_display=('course_name','course_poster','course_details')

admin.site.register(course_details, course_admin)

