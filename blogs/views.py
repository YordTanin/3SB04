from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User,auth
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def index(request):
    #Query Data From Model
    data=Post.objects.all()
    return render(request,'index.html',{'posts':data})
    
def page1(request):
    return render(request,'page1.html')
def createForm(request):
    return render(request,'form.html')
def loginForm(request):
    return render(request,'login.html')
def addUser(request):
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['repassword']
   
    if password==repassword :
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username นี้มีคนใช้แล้ว')
            return redirect('/createForm')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email นี้มีคนใช้แล้ว')
            return redirect('/createForm')
        else:
            user=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname
            )
            user.save()
            return redirect('/index')
    else:
        messages.info(request, 'รหัสผ่านไม่ตรงกัน')
        return redirect('/createForm')
def login(request):
    username=request.POST['username']
    password=request.POST['password']
    
    #login
    user=auth.authenticate(username=username,password=password) 

    if user is not None :
        auth.login(request, user)
        return redirect('/index')
    else:
        messages.info(request,'ไม่พบข้อมูล')
        return redirect('/loginForm')
def logout(request):
    auth.logout(request)
    return redirect('/index')