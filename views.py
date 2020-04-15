# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

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
#_________________________________________________________________________________

def confirm(request):
    djname=request.GET.get('name','default')
    djtext=request.GET.get('text','default')
    by='- by '
    print("{} is the received input from server".format(djtext))
    params={'djname':djname,'djtext': djtext,'djby':by}
    return render(request,'blog/mauri.html',params)

#_________________________________________________________________________________
#SignUp
def signup(request):
    if(request.method=="POST"):
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password1 = request.POST['password1']
        passwor2 = request.POST['password2']
        
        # form validation 
        if not username.isalnum():
            messages.error(request,'atleast 1 letter and number required')
            return redirect('blog')
        if(passwor2!=password1):
            messages.error(request,'Passwords do not match')
            return redirect('blog')
        #
        myuser= User.objects.create_user(username,  password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request ,"Account created Successfully")
        return redirect('blog ')
    else:
        return HttpResponse("404 - Page Not found")

#Login
#____________________________________________________________________________________

def handleLogin(request):
    if(request.method=="POST"):
        Lusername=request.POST[uname]
        Lpassword=request.POST[passwd]

        #authentication
        user= authenticate(username=Lusername , password=Lpassword)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully logged in")
    else:
        return messages.error(request,'404')
    return HttpResponse('handleLogin')

#________________________________________________________________________________________
#Logout

def handleLogout(request):

    return HttpResponse('handleLogout')
  