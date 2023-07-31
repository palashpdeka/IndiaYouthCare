from django.urls import path,include
from . import views

urlpatterns = [
    path('career/', views.career_page),
]