from django.contrib import admin
from courses.models import course_details,registrant

class course_admin(admin.ModelAdmin):
    list_display=('course_name','course_poster','course_details')

class registrant_admin(admin.ModelAdmin):
    list_display=('name','email','phone','course','comment')

admin.site.register(course_details, course_admin)
admin.site.register(registrant, registrant_admin)

