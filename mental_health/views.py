from django.shortcuts import render
from django.http import HttpResponse

def mental_health_page(request):
    return render(request,"mental_health.html")
