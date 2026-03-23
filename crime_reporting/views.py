from django.shortcuts import render,redirect
from crime_reporting import models
from django.contrib import messages
from django.contrib.sessions.models import Session

def home(request):
    return render(request,'home/home.html')

def login(request):
    return render(request,'login/login.html')



def check_login(request):
    username = request.POST["email"]
    password = request.POST["password"]
    # return HttpResponse(username1)
    log_info = models.Login.objects.filter(username=username,password=password)
    # return HttpResponse(log_info)
    for info in log_info:
        if info.username == username and info.password==password:
            if info.user_type == 'admin':
                request.session['semail'] = info.username
                request.session['user_type'] = info.user_type
                return redirect("../administrator/admin")
            elif info.user_type == 'citizen':
                request.session['semail'] = info.username
                request.session['user_type'] = info.user_type
                return redirect("../citizens/citizen")
            elif info.user_type == 'investigator':
                request.session['semail'] = info.username
                request.session['user_type'] = info.user_type
                return redirect("../investigators/inv_dashboard")
            
        messages.success(request,"invalid username or password")
        return redirect('login')
    messages.success(request,"invalid username or password")
    return redirect('login')
def logout(request):
  Session.objects.all().delete()
  return redirect('home')
def registration(request):
    return render(request,'home/registration.html')
def citizen_save(request):
    name=request.POST['full_name']
    email=request.POST['user_email']
    phno=request.POST['user_phone']
    address=request.POST['user_address']
    location=request.POST['user_location']
    gender=request.POST['gender']
    password=request.POST['password']
    existing_user = models.Login.objects.filter(username=email).first()
    if existing_user:
        messages.warning(request,'Email Id already exists!!!!!')
        return redirect('registration')
    investigator_data=models.Users(full_name=name,user_email=email,user_phone=phno,user_address=address,user_location=location,user_gender=gender,user_role='citizen')
    investigator_data.save()
    log_data=models.Login(username=email,password=password,user_type='citizen',user_status='active')
    log_data.save()
    messages.success(request,"Registered successfully")
    return redirect('login')