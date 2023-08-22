from django.shortcuts import render,redirect
from .models import *

def booking(request):
    return render(request,'booking.html')

def index(request):
    userdata = UserDetail.objects.all()
    return render(request, 'index.html',{'userdata':userdata})
def home(request):
    return render(request,"home.html")

def userDetailsAdd(request):
    name=request.POST['name']
    email=request.POST['email']
    checkin=request.POST['checkin']
    checkout = request.POST['checkout']
    UserDetail.objects.create(name=name,email=email,checkin=checkin,checkout=checkout).save()
    return redirect('/')

def edituser(request,id):
    userdata=UserDetail.objects.get(id=id)
    return render(request,'edituser.html',{'userdata':userdata})
def userDetailsUpdate(request,id):
    name=request.POST['name']
    email=request.POST['email']
    checkin = request.POST['checkin']
    checkout = request.POST['checkin']
    UserDetail.objects.filter(id=id).update(name=name,email=email,checkin=checkin,checkout=checkout).save()
    return redirect('/')
def userDetailsDelete(request,id):
    UserDetail.objects.filter(id=id).delete()
    return redirect('/')



