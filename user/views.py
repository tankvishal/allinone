from ast import Not, NotIn
from email.headerregistry import Address
from lib2to3.pgen2.token import RIGHTSHIFTEQUAL
from multiprocessing import context
from operator import not_
import re
from tkinter.tix import Form
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse
from allinone import settings
from django.contrib.auth.decorators import login_required
# from requests import request
from .models import Agent, Customer,Contactform, Kyc, Orderlist, Payment, Service, Subservice
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib import messages
from time import gmtime, strftime
from django.contrib.auth.models import User
import random
from datetime import datetime

# Create your views here.
def home(request):
    # allService=Service.objects.all()
    # context={'Services':allService}
    # print(allService)
    return render(request,"user/home.html")

# def navbar(request):
#     return render(request,"user/navbar.html")


def tc(request):
    return render(request,"user/terms-conditions.html")

def about(request):
    return render(request,"user/about-us.html")

def contect(request):
    return render(request,"user/contect-us.html")
    
def registert(request):
    return render(request,"user/register-type.html")

def uagentregister(request):
    return render(request,"user/agent-register.html")

@login_required(login_url="/login/")
def adminpan(request):
    return render(request,"adminpan/index.html")

def admindash(request):
    return render(request,"user/admindash.html")

def serviceuser(request):
    allService=Service.objects.all()
    context={'Services':allService}
    print(allService)
    return render(request,"user/services.html",context)

@login_required(login_url="/login/")
def customerdash(request):
    allService=Service.objects.all()
    context={'Services':allService}
    print(allService)
    return render(request,"coustomer/customerdash.html",context)

# def coustomer(request):
    
#     return render(request,"coustomer/customerdash.html")

def electricians(request,id):
    allSubservice=Subservice.objects.filter(serviceid=id)
    allService=Service.objects.get(pk=id)
    context={'Subservice':allSubservice,'Servicedata':allService}
    print(allSubservice)
    return render(request,"user/electricians.html",context)

def homepainting(request):
    return render(request,"user/home-painting.html")

def carpanter(request):
    return render(request,"user/carpanter.html")

def plumber(request):
    return render(request,"user/plumber.html")

def login_user(request):
    if request.method == "POST":
        username=request.POST['email']
        password=request.POST['pass']
        print(username)
        print(password)
        user=authenticate(request,username=username,password=password)
        print(user)
        if user:
            print("hello")
            if user.is_superuser==True:
                login(request,user)
                return redirect("adminpan")
            elif user.is_staff == True:
                login(request,user)
                return redirect("agentindex")
            else:
                login(request,user)
                return redirect("customerdash")
        else:
            return redirect('login')
    return render(request,'user/login.html')

def forgetpass(request):
    return render(request,"user/forget-password.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        useremail = request.POST.get('email')
        userpassword = request.POST.get('pass')
        # pass2 = request.POST.get('password2')
        usermobileno = request.POST.get('mno')
        usergender = request.POST.get('Gender')
        useraddress=request.POST.get('address')
        print(username)
        userstutas = False
        # print("arjun")
        user=User.objects.create(username=username,email=useremail,password=make_password(userpassword))
        C=Customer(username=username,useremail=useremail,userpassword=userpassword,usermobileno=usermobileno,usergender=usergender,useraddress=useraddress,userstutas=userstutas)
        C.save()
        return redirect('login')
    return render(request,"user/register.html")


def signup_agent(request):
    if request.method=="POST":
        agentname=request.POST.get('uname')
        agentemail = request.POST.get('email')
        agentgender = request.POST.get('Gender')
        agentpassword = request.POST.get('pass')
        agentmobileno = request.POST.get('mno')
        agentaddress=request.POST.get('address')
        agentspealist=request.POST.get('Specialist')
        agentkycstutas = False
        agentstutas = False
        user=User.objects.create(username=agentname,email=agentemail,password=make_password(agentpassword),is_staff=True)
        A=Agent(agentname=agentname,agentemail=agentemail,agentgender=agentgender,agentpassword=agentpassword,agentmobileno=agentmobileno,agentaddress=agentaddress,agentspealist=agentspealist,agentkycstutas=agentkycstutas,agentstutas=agentstutas)
        user.is_staff = True
        A.save()
        return redirect('login')
    return render(request,"user/agent-register.html")




def contect(request):
    if request.method=="POST":
        contactname = request.POST.get('fullname')
        contactemail = request.POST.get('email')
        contactmobileno = request.POST.get('phone')
        contactmessage = request.POST.get('Message')
        cc=Contactform(contactname=contactname,contactemail=contactemail,contactmobileno=contactmobileno,contactmessage=contactmessage)
        cc.save()
        return redirect('contect')
    return render(request,"user/contect-us.html")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def bookele(request):
    if request.user.is_authenticated:
        return render(request,"user/bookele.html")
    return HttpResponseRedirect('/login/')

# coustomer pages


# agent panel
@login_required(login_url="/login/")
def agentindex(request):
    return render(request,"agent/agentindex.html") 




@login_required(login_url="/login/")
def agentpayment(request):
    allPayment=Payment.objects.all()
    context={'Payments':allPayment}
    print(allPayment)
    return render(request,"agent/agentpayment.html",context) 

@login_required(login_url="/login/")
def agentorderlist(request):
    agent = Agent.objects.get(agentname=request.user.username)
    allOrderlist=Orderlist.objects.filter(agentid=agent.agentid)
    context={'Orderlists':allOrderlist}
    print(allOrderlist)
    return render(request,"agent/agentorderlist.html",context) 

@login_required(login_url="/login/")
def agentprofile(request):
    agent = Agent.objects.get(agentname=request.user.username)
    allKyc=Kyc.objects.get(agentid=agent.agentid)
    context={'kyc':allKyc}
    return render(request,"agent/agentprofile.html",context) 


@login_required(login_url="/login/")
def agentnotification(request):
    allOrderlist=Orderlist.objects.filter(orderstutas=False)
    context={'Orderlists':allOrderlist}
    print(allOrderlist)
    return render(request,"agent/agentnotification.html",context) 


@login_required(login_url="/login/")
def agentkycdetail(request):
    agent = Agent.objects.get(agentname=request.user.username)
    context = {'agent':agent}
    if request.method=="POST":
        agentid = request.POST.get('agentid')
        agentaadharno= request.POST.get('adharno')
        agentpanno= request.POST.get('panno')
        agentaccountno= request.POST.get('acctno')
        agentifsccode=request.POST.get('ifsccode')
        agentbankname=request.POST.get('bankname')
        agentaadharimg=request.FILES.get('adharimg')
        agentpanimage=request.FILES.get('panimg')
        agentpassbookimage=request.FILES.get('bankimg')
        agentimage=request.FILES.get('aimg')
        s=Kyc(agentid=agentid,agentaadharno=agentaadharno,agentpanno=agentpanno,
              agentaccountno=agentaccountno,agentifsccode=agentifsccode,agentbankname=agentbankname,
              agentaadharimg=agentaadharimg,agentpanimage=agentpanimage,agentpassbookimage=agentpassbookimage,agentimage=agentimage)
        s.save()
        return redirect('agentkycdetail')
    return render(request,"agent/agentkycdetail.html",context)
    
    
@login_required(login_url="/login/")
def insertorder(request):
    if request.method=="POST":
        userid = request.POST.get('userid')
        serviceid= request.POST.get('serviceid')
        subserviceid= request.POST.get('subserviceid')
        subservicename= request.POST.get('subservicename')
        serviceprice=int(float(request.POST.get('serviceprice')))
        houseno=request.POST.get('houseno')
        landmark=request.POST.get('landmark')
        area=request.POST.get('area')
        pincode=request.POST.get('pincode')
        otp = random.randint(1111,9999)
        address = str(houseno)+", "+str(landmark)+", "+str(area)+" - "+str(pincode)
        current_datetime = datetime.now()  
        orderdate = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        order =Orderlist(userid=userid,agentid=0,orderotp=otp,serviceid=serviceid,subserviceid=subserviceid,servicename=subservicename,orderprice=serviceprice,orderaddress=address,ordercompletetime=orderdate,orderdatetime=orderdate,orderstutas=0) 
        order.save()
        payment(request,userid,serviceprice,orderdate)
        return redirect('bookingongoing')
    return render(request,"agent/agentkycdetail.html")
     
def payment(request,userid,amount,paymenttime):
    order = Orderlist.objects.get(orderdatetime=paymenttime)
    payment = Payment(userid=userid,orderid=order.orderid,amount=amount,paymentdatetime=paymenttime,paymentstutas=1)
    payment.save()
    
@login_required(login_url="/login/")
def agentedits(request):
    return render(request,"agent/agentedits.html")


@login_required(login_url="/login/")
def cbookele(request,id):
    allSubservice=Subservice.objects.get(subserviceid=id)
    useridata = Customer.objects.get(username=request.user.username)
    # allService=Service.objects.get(pk=id)
    context={'Subservice':allSubservice,"userid":useridata}
    # print(allSubservice)
    return render(request,"coustomer/cbookele.html",context)

@login_required(login_url="/login/")
def celectricians(request,id):
    allSubservice=Subservice.objects.filter(serviceid=id)
    allService=Service.objects.get(pk=id)
    context={'Subservice':allSubservice,'Servicedata':allService}
    print(allSubservice)
    return render(request,"coustomer/celectricians.html",context)

@login_required(login_url="/login/")
def chomepainting(request):
    return render(request,"coustomer/chome-painting.html")

@login_required(login_url="/login/")
def ccarpanter(request):
    return render(request,"coustomer/ccarpanter.html")

@login_required(login_url="/login/")
def cplumber(request):
    return render(request,"coustomer/cplumber.html")

@login_required(login_url="/login/")
def mybooking(request):
    return render(request,"coustomer/mybooking.html")
  
@login_required(login_url="/login/")
def transaction(request):
    return render(request,"coustomer/transaction.html")

@login_required(login_url="/login/")
def fedback(request):
    return render(request,"coustomer/fedback.html")

@login_required(login_url="/login/")
def notification(request):
    return render(request,"coustomer/notification.html")

@login_required(login_url="/login/")
def bookingongoing(request):
    useridata = Customer.objects.get(username=request.user.username)
    allService=Orderlist.objects.filter(userid=useridata.userid,orderstutas=False)
    context={'ongoingbook':allService}
    return render(request,"coustomer/bookingongoing.html",context)

@login_required(login_url="/login/")
def bookinghistory(request):
    useridata = Customer.objects.get(username=request.user.username)
    allService=Orderlist.objects.filter(userid=useridata.userid,orderstutas=True)
    context={'bookhistory':allService}
    return render(request,"coustomer/bookinghistory.html",context)

@login_required(login_url="/login/")
def viewbooking(request,id):
    orderdetail=Orderlist.objects.get(orderid=id)
    agent = Kyc.objects.get(agentid=orderdetail.agentid)
    context={'orderdetail':orderdetail,'agent':agent}
    return render(request,"coustomer/viewbooking.html",context)

@login_required(login_url="/login/")
def profileedit(request):
    return render(request,"coustomer/profile-edit.html")

@login_required(login_url="/login/")
def profile(request):
    return render(request,"coustomer/profile.html")

@login_required(login_url="/login/")
def vieworderdetail(request):
    return render(request,"agent/vieworderdetail.html")

@login_required(login_url="/login/")
def viewnotificationdetails(request,id):
    orderlist=Orderlist.objects.get(pk=id)
    userdetails=Customer.objects.get(userid=orderlist.userid)
    context={'Orderlist':orderlist,"userdetails":userdetails}
    return render(request,"agent/viewnotificationdetails.html",context)

@login_required(login_url="/login/")
def orderaccept(request,id):
    current_datetime = datetime.now()
    orderdate = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    agent = Agent.objects.get(agentname=request.user.username)
    orderlist=Orderlist.objects.filter(pk=id).update(agentid=agent.agentid,ordercompletetime=orderdate,orderstutas=True)
        # return redirect('agentnotification')
    return HttpResponseRedirect(reverse("agentnotification"))