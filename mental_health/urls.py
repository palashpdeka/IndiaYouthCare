from django.urls import path,include
from . import views

urlpatterns = [
    path('mental_health/', views.mental_health_page),
]