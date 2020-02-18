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


def lisa_kiarie(request):
    title='Lisa'
    return render(request,"lisa_kiarie.html",{"title":title})    


def about(request):
    title='About'
    return render(request,"about.html",{"title":title})        

 
def lisa_blogs(request):
    title='Blogs'
    return render(request,"lisa_blogs.html",{"title":title}) 


def faq(request):
    title='Faq'
    return render(request,"faq.html",{"title":title})  