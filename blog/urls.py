from django.urls import path,include
from . import views

urlpatterns = [
    path('blogs/', views.blogs_page),
    path('write_blog/', views.write_blog),
    path('save_blog/', views.save_blog, name="save_blog"),
]