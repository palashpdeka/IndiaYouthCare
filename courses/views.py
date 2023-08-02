from django.shortcuts import render
from django.http import HttpResponse
from courses.models import course_details

def courses_page(request):
    all_courses=course_details.objects.all()
    data={'courses':all_courses}
    return render(request,"courses.html",data)
