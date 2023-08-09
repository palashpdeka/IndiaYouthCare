from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import blog_info
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import path
import datetime, os, time

def blogs_page(request):
    all_blogs=blog_info.objects.filter(status='a')
    data={'blogs':all_blogs}
    return render(request,"blogs.html",data)

# @receiver(pre_delete, sender=blog_info)
# def blog_info_image(sender, instance, **kwargs):
#     os.remove(kwargs['origin'].image.path)


def write_blog(request):
    return render(request,"write_blog.html")

def save_blog(request):
    if request.method=='POST':
       name_=request.POST.get('name')
       email_=request.POST.get('email')
       link_=request.POST.get('link')
       comment_=request.POST.get('comment')
       curr_date=datetime.date.today()
       curr_time=time.strftime("%H:%M:%S", time.localtime())
       var=blog_info(name=name_, email=email_, link=link_, comment=comment_, status='r', time=curr_time, date=curr_date)
       var.save()
    return redirect("/blogs")