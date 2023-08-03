from django.shortcuts import render
from django.http import HttpResponse
from courses.models import course_detail, registrant
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import path
import datetime, os


def courses_page(request):
    all_courses=course_detail.objects.all()
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

@receiver(pre_delete, sender=course_detail)
def delete_course_image(sender, instance, **kwargs):
    os.remove(kwargs['origin'].course_poster.path)