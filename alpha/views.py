from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
# import requests
# Create your views here.
def index(request):
    title='Home'
    return render(request,"index.html",{"title":title})

def talent_management(request):
    title='Talent'
    return render(request,"talent_management.html",{"title":title})