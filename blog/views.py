from django.shortcuts import render
from django.http import HttpResponse
from blog.models import blog_info
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import path
import datetime, os

def blogs_page(request):
    all_blogs=blog_info.objects.all()
    data={'blogs':all_blogs}
    return render(request,"blogs.html",data)

@receiver(pre_delete, sender=blog_info)
def blog_info_image(sender, instance, **kwargs):
    os.remove(kwargs['origin'].image.path)