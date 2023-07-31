from django.shortcuts import render

def hompage(request):
    return render(request,"homepage.html")

def header(request):
    return render(request,"header.html")