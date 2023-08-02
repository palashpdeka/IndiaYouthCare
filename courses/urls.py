from django.urls import path,include
from . import views

urlpatterns = [
    path('courses/', views.courses_page),
    path('regnForm/', views.regnForm,name="regn_form"),
    path('save_details/', views.save_details, name="save_details"),
]