from django.shortcuts import render
from django.http import HttpResponse

def about_us_page(request):
    return render(request,"about_us.html")
