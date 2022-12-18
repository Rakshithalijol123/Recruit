import email
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if fname == "":
            messages.error(request,"First Name cannot be empty")
            return redirect('register')
        if lname == "":
            messages.error(request,"Last Name cannot be empty")
            return redirect('register')
        if email == "":
            messages.error(request,"E-Mail cannot be empty")
            return redirect('register')
        if username == "":
            messages.error(request,"Username cannot be empty")
            return redirect('register')
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"E-Mail already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=pass1)
                user.save()
                messages.success(request,"Successfully Signed In")
                return redirect('login')
        else:
            messages.error(request,"Password Mismatches")
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if password == "":
            messages.error(request,"Password cannot be empty")
            return redirect('login')
        if username == "":
            messages.error(request,"Username cannot be empty")
            return redirect('login')
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Successfully Logged-In")
            return redirect('/')
        else:
            messages.error(request,"Invalid Details")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
