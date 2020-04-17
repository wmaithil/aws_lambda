# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.
def blog(request):
    return render(request,'blog/index.html')

def cover(request): 
    return render(request,'blog/cover.html')

def home(request):
    return render(request,'blog/bloghome.html')


def mauritius(request):
    if (request.method=="POST"):
        djname = request.POST['name']
        djtext = request.POST['text']
        print ("djtext :{}".format(djtext) )
        by='by '
        print("{} is the received input from server".format(djtext))
        params={'djname':djname,'djtext': djtext,'djby':by}
        return render(request,'blog/mauri.html',params)
    return render(request,'blog/mauri.html')
   

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
    if(request.method == "POST"):
        fname = request.POST['fname']
        print(fname)
        lname = request.POST['lname']
        print(lname)
        username = request.POST['username']
        print(username)
        emailid = request.POST['emailid']
        print(emailid)
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # form validation 
        if not username.isalnum():
            messages.error(request,'atleast 1 letter and number required')
            print("alnum condition checked")
            return redirect('blog')

        if(password2 != password1):
            print("password condition checked")
            messages.error(request,'Passwords do not match')
            #return redirect('blog')
            return redirect('blog')
        #
        myuser= User.objects.create_user(username, emailid ,password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        print("user created")
        messages.success(request ,"Account created Successfully")
        return redirect('blog')
    else:
        return HttpResponse("404 - Page Not found")

#Login
#____________________________________________________________________________________

def handleLogin(request):
    if(request.method == "POST"):
        lusername = request.POST['loginusername']
        lpassword = request.POST['loginpassword']
        print("username recieved")

        #authentication
        user= authenticate(username=lusername , password=lpassword)
        print("Authentication done")

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully logged in")
            print("Successfully logged in")
            return redirect('blog')
        else:
            print("authentication issues")
            messages.error(request,'Invalid credentials')
            return redirect('blog')

    return HttpResponse('404 page not found')

#________________________________________________________________________________________
#Logout

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('blog') 
    
  