from django.contrib import admin
from courses.models import course_detail,registrant

class course_admin(admin.ModelAdmin):
    list_display=('course_name','course_poster','course_info')

class registrant_admin(admin.ModelAdmin):
    list_display=('name','email','phone','course','comment')

admin.site.register(course_detail, course_admin)
admin.site.register(registrant, registrant_admin)

