# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def login(request):
    return render(request,'blog/signin.html')

def cover(request):
    return render(request,'blog/cover.html')

def home(request):
    return render(request,'blog/bloghome.html')