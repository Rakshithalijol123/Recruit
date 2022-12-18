from turtle import position
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Internship,Contact,Resume
from django.contrib import messages
from datetime import datetime
# Create your views here.

def index(request):
    internships = Internship.objects.all()
    return render(request,'index.html',{'internships':internships[:5]})

def about(request):
    return render(request,'about.html')

def resume(request):
    if request.method == "POST":
        user = request.user
        resume_file = request.FILES['resume_file']
        resume = Resume.objects.create(user=user,resume_file=resume_file)
        resume.save()
        messages.success(request,"Your Resume has been successfully submitted..!!")
    return render(request,'resume.html')

def res(request):
    return render(request,'res.html')

def view_all_internships(request):
    if request.user.is_authenticated:
        all_internships = Internship.objects.all()
        return render(request,'internships.html',{"all_internships":all_internships})
    else:
        return redirect('login')

def detail_abt_internship(request,id):
    if request.user.is_authenticated:
        that_internship = Internship.objects.filter(id=id)
        return render(request,'detail_abt_internship.html',{'that_internship':that_internship})
    else:
        return redirect('login')
    

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        tell_me = request.POST.get('tell_me')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        if request.user.is_authenticated:
            contact = Contact(fname=fname,lname=lname,email=email,phno=phno,tell_me=tell_me,address=address,address2=address2,city=city,zip=zip)
            contact.save()
            messages.success(request,"Your message has been sent..!!")
            # return redirect('contact')
        else:
            messages.error(request,"Please Log In")
            return redirect('login')
    return render(request,'contact.html')

def IT_cat(request):
    if request.user.is_authenticated:
        it_internships = Internship.objects.filter(category="IT")
        return render(request,'internships.html',{'it_internships':it_internships})
    else:
        return redirect('login')


def Mech_cat(request):
    if request.user.is_authenticated:
        mech_internships = Internship.objects.filter(category="Mechanical")
        return render(request,'internships.html',{'mech_internships':mech_internships})
    else:
        return redirect('login')
    

def Ece_cat(request):
    if request.user.is_authenticated:
        ec_internships = Internship.objects.filter(category="Electronics")
        return render(request,'internships.html',{'ec_internships':ec_internships})
    else:
        return redirect('login')
    

def Mrk_cat(request):
    if request.user.is_authenticated:
        mrkt_internships = Internship.objects.filter(category="Marketing")
        return render(request,'internships.html',{'mrkt_internships':mrkt_internships})
    else:
        return redirect('login')
    
# def intern_resume(request):
#     if request.method == "POST":
#         resume_file = request.FILES['resume_file']
#         resume = Resume.objects.create(resume_file=resume_file)
#         resume.save()
#         print("<<<<<<<<<<<<<<<<<<<<<<<File Saved>>>>>>>>>>>>>>>>>>>>>>>>>")
#         messages.success(request,"Your Resume has been successfully submitted..!!")
#     return render(request,'resume.html')


# def search(request):
#     if request.method == "POST": 
#         items = request.POST.get('items')
#         # print(f"+++++++++++++++++++++    {items}    +++++++++++++++++++++")
#         if items != ' ':
#             item_detial = Icecream.objects.filter(name = items)
#             # print(f"+++++++++++++++++++++    {item_detial}    +++++++++++++++++++++")
#             return render(request,'search.html',{'item_detial':item_detial})
#         else:
#             messages.error(request,'Item not found')
#             return redirect('/')
#     return render(request,'index.html') 

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        retrive_int = Internship.objects.all()
            # print(f"**********************{item.position}*******************************")
        if search:
            searched_internship = Internship.objects.filter(position=search)
            return render(request,'search.html',{'searched_internship':searched_internship})
        else:
            messages.error(request,'Position not found')
            return redirect('/') 
    return render(request,'index.html') 

def congrats(request):
    return render(request,'congrats.html')
        
    