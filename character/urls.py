from django.urls import path,include
from . import views

urlpatterns = [
    path('character/', views.character_page),
]