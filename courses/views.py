from django.shortcuts import render
from django.http import HttpResponse

def courses_page(request):
    return render(request,"courses.html")
