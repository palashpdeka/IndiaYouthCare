from django.shortcuts import render
from django.http import HttpResponse
from courses.models import course_details, registrant
import datetime

def courses_page(request):
    all_courses=course_details.objects.all()
    data={'courses':all_courses}
    return render(request,"courses.html",data)

def regnForm(request):
    if request.method=='POST':
       c_name=request.POST.get('course_name')
    return render(request,"regnForm.html",{'course':c_name})

def save_details(request):
    if request.method=="POST":
       name_=request.POST.get('name')
       email_=request.POST.get('email')
       phone_=request.POST.get('phone')
       comment_=request.POST.get('comment')
       course_=request.POST.get('course')
       curr_time=datetime.datetime.now()
       var=registrant(name=name_, email=email_, phone=phone_, comment=comment_, course=course_, time=curr_time)
       #print(name_, email_, phone_, comment_, course_, curr_time)
       var.save()
    all_courses=course_details.objects.all()
    data={'courses':all_courses}
    return render(request,"courses.html",data)
