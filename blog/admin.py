from django.contrib import admin
from blog.models import blog_info

class blog_info_admin(admin.ModelAdmin):
    list_display=('name','comment','social_media','link','date','time')

admin.site.register(blog_info, blog_info_admin)