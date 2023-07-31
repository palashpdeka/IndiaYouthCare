from django.shortcuts import render
from django.http import HttpResponse

def career_page(request):
    return render(request,"career.html")
