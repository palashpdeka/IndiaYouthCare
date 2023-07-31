from django.shortcuts import render
from django.http import HttpResponse

def character_page(request):
    return render(request,"character.html")
