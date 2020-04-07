# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'blog/index.html')
 
def login(request):
    return render(request,'blog/si?name=Maithil+R+Wadehg&text=ydcdach+cudchdb+dcbgnin.html')

def cover(request): 
    return render(request,'blog/cover.html')

def home(request):
    return render(request,'blog/bloghome.html')

def blogpost(request):
    return render(request,'blog/blogpost.html')

def mauritius(request):
    if (request.method=="GET"):
        djname=request.GET.get('name',' ')
        djtext=request.GET.get('text','')
        by='by '
        if (djtext):
            pass
        if(djname==' ' or djtext=="notok"):
            by=' '
        print("{} is the received input from server".format(djtext))
        params={'djname':djname,'djtext': djtext,'djby':by}
        return render(request,'blog/mauri.html',params)
   

def sunset(request):
    return render(request,'blog/sunset.html')

def beach(request):
    return render(request,'blog/beach.html')

def confirm(request):
    djname=request.GET.get('name','default')
    djtext=request.GET.get('text','default')
    by='- by '
    print("{} is the received input from server".format(djtext))
    params={'djname':djname,'djtext': djtext,'djby':by}
    return render(request,'blog/mauri.html',params)
  