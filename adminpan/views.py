from asyncio import all_tasks
from multiprocessing import context
import re
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
# from allinone.user.models import Feedback
# from allinone.user.models import Kyc
# from allinone.user.models import Contactform
# from allinone.user.models import Payment
# from scipy.fft import idct
from user.models import Agent, Customer, Orderlist, Service,Subservice,Payment,Contactform,Kyc,Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# from user.models import GetImage
# from requests import request

# Create your views here.
# def index(request):
#     return render(request,"index.html")

# Create your views here.
@login_required(login_url="/login/")
def adminpan(request):
    customer=Customer.objects.all()
    customer_count=customer.count()
    agent=Agent.objects.all()
    agent_count=agent.count()
    service=Orderlist.objects.all()
    service_pending = service.filter(orderstutas='False').all()
    service_complete = service.filter(orderstutas='True').all()
    context={
        'customer':customer,
        'customer_count':customer_count,
        'agent_count':agent_count,
        'service_pending':service_pending,
        'service_complete':service_complete
        }
    return render(request,"index.html",context)

@login_required(login_url="/login/")
def agent(request):
    allAgent=Agent.objects.all()
    context={'Agents':allAgent}
    return render(request,"agent.html",context)


@login_required(login_url="/login/")
def services(request):
    allService=Service.objects.all()
    context={'Services':allService}
    print(allService)
    return render(request,"services.html",context)


# def Table(request):
#     return render(request,"table-list.html")

# def users(request,id):
#     allCustomer=Customer.objects.all()
#     context={'Customers':allCustomer}
#     return render(request,"users.html",context)

@login_required(login_url="/login/")
def users(request):
    allCustomer=Customer.objects.all()
    context={'Customers':allCustomer}
    return render(request,"users.html",context)

# def services(request):
#     return render(request,"services.html")


# def subservice(request):
#     allSubcategory=Subservice.objects.all()
#     context={'Subcategorys':allSubcategory}
#     return render(request,"sub-service.html",context)
    
@login_required(login_url="/login/")
def subservices(request):
    allsubservice=Subservice.objects.all()
    context={'Subservices':allsubservice}
    return render(request,"sub-services.html",context)

@login_required(login_url="/login/")
def payment(request):
    allpayment=Payment.objects.all()
    context={'Payments':allpayment}
    return render(request,"payment.html",context)

@login_required(login_url="/login/")
def contectus(request):
    allcontactform=Contactform.objects.all()
    context={'Contactforms':allcontactform}
    return render(request,"Contect-Us.html",context)

#  {% for contactform in Contactforms %}
# {% for kyc in kycs %} 

@login_required(login_url="/login/")
def agentkyc(request):
    allkyc=Kyc.objects.all()
    context={'Kycs':allkyc}
    return render(request,"agentkyc.html",context)

def feedback(request):
    allFeedbacks=Feedback.objects.all()
    context={'Feedbacks':allFeedbacks}
    return render(request,"feedback.html",context)

@login_required(login_url="/login/")
def order(request):
    allorderlist=Orderlist.objects.all()
    context={'Orderlists':allorderlist}
    return render(request,"order-list.html",context)

@login_required(login_url="/login/")
def setting(request):
    return render(request,"setting.html")

@login_required(login_url="/login/")
def useredit(request,id):
    customerdata=Customer.objects.get(pk=id)
    context={'Customerdata':customerdata}
    return render(request,'user-edit.html',context)
    
@login_required(login_url="/login/")
def agentedit(request,id):
    agentdata=Agent.objects.get(pk=id)
    context={'Agentdata':agentdata}
    return render(request,'agent-edit.html',context)

@login_required(login_url="/login/")
def servicesedit(request,id):
    servicedata=Service.objects.get(pk=id)
    context={'Servicedata':servicedata}
    return render(request,"services-edit.html",context)


@login_required(login_url="/login/")
def subservicesedit(request,id):
    subservicedata=Subservice.objects.get(pk=id)
    allService=Service.objects.all()
    context={'Subservice':subservicedata,'Services':allService}
    return render(request,"subservices-edit.html",context)

@login_required(login_url="/login/")
def addsubservices(request):
    return render(request,"add-subservices.html")


@login_required(login_url="/login/")
def delete_data_customer(request,id):
    pi=Customer.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect(reverse("users"))
   
@login_required(login_url="/login/") 
def delete_data_agent(request,id):
    pi=Agent.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect(reverse("agent"))

@login_required(login_url="/login/") 
def delete_data_orderlist(request,id):
     pi=Orderlist.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect(reverse("order"))

@login_required(login_url="/login/")
def delete_data_payment(request,id):
     pi=Payment.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect(reverse("payment"))
 
@login_required(login_url="/login/")
def delete_data_contact(request,id):
     pi=Contactform.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect(reverse("payment"))

@login_required(login_url="/login/")
def delete_data_kyc(request,id):
     pi=Kyc.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect(reverse("agentkyc"))
 
@login_required(login_url="/login/") 
def delete_data_feedback(request,id):
     pi=Feedback.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect(reverse("feedback"))
 
@login_required(login_url="/login/") 
def delete_data_service(request,id):
     pi=Service.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect(reverse("services"))
 
@login_required(login_url="/login/") 
def delete_data_subservice(request,id):
     pi=Subservice.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect(reverse("subservices"))
 
   
# def delete_data_category(request,id):
#     pi=Category.objects.get(pk=id)
#     pi.delete()
#     return HttpResponseRedirect(reverse("Category"))

@login_required(login_url="/login/")
def delete_data_subcategory(request,id):
    pi=Subservice.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect(reverse("Category"))
    
@login_required(login_url="/login/")
def update_data_customer(request):
    if request.method =='POST':
        uid=request.POST.get('uid')
        username=request.POST.get('uname')
        useremail = request.POST.get('email')
        useraddress = request.POST.get('address')
        userpassword = request.POST.get('pass')
        usermobileno = request.POST.get('mno')
        usergender=request.POST.get('Gender')
        userstutas = request.POST.get('Status')
        if userstutas == "0":
            userstutas = False
        else:
            userstutas = True
        C=Customer.objects.filter(userid=uid).update(username=username,useremail=useremail,useraddress=useraddress,userpassword=userpassword,usermobileno=usermobileno,usergender=usergender,userstutas=userstutas)
        # C.save()
        return redirect('users')
    return render(request,"user-edit.html",context)

@login_required(login_url="/login/")
def update_data_user(request):
    if request.method =='POST':
        aid=request.POST.get('cid')
        agentname=request.POST.get('uname')
        agentmobileno = request.POST.get('mno')
        agentemail = request.POST.get('email')
        agentgender = request.POST.get('Gender')
        agentspealist = request.POST.get('Specialist')
        agentaddress=request.POST.get('address')
        agentkycstutas=request.POST.get('kycStatus')
        agentstutas = request.POST.get('Status')
        a=Agent.objects.filter(agentid=aid).update(agentname=agentname,agentmobileno=agentmobileno,agentemail=agentemail,agentgender=agentgender,agentspealist=agentspealist,agentaddress=agentaddress,agentkycstutas=agentkycstutas,agentstutas=agentstutas)
        # C.save()
        return redirect('agent')
    return render(request,"agent-edit.html",context)

@login_required(login_url="/login/")
def update_data_subservice(request):
    if request.method =='POST':
        subserviceid=request.POST.get('subserviceid')
        serviceid= request.POST.get('serviceid')
        subservicename=request.POST.get('subservicename')
        subservicedescription = request.POST.get('subservicedescription')
        subserviceimage = request.POST.get('subserviceimg')
        subserviceprice = request.POST.get('subserviceprice')
        subservicestutas = request.POST.get('Status')
        sub=Subservice.objects.filter(subserviceid=subserviceid).update(serviceid=serviceid,subservicename=subservicename,subservicedescription=subservicedescription,subserviceimage=subserviceimage,subserviceprice=subserviceprice,subservicestutas=subservicestutas)
        # C.save()
        return redirect('subservices')
    return render(request,"subservices-edit.html",context)

@login_required(login_url="/login/")
def update_data_service(request):
    if request.method=="POST":
        sid = request.POST.get('serviceid')
        servicename = request.POST.get('servicename')
        servicedescription = request.POST.get('servicedescription')
        serviceimage = request.POST.get('serviceimg')
        servicestutas= request.POST.get('ServiceStatus')
        z=Service.objects.filter(serviceid=sid).update(servicename=servicename,servicedescription=servicedescription,serviceimage=serviceimage,servicestutas=servicestutas)
        # z.save()
        return redirect('services')
    return render(request,"add-services.html")

# def update_data_service(request):
#     if request.method =='POST':
#         sid=request.POST.get('sid')
#         agentname=request.POST.get('uname')
#         agentmobileno = request.POST.get('mno')
#         a=Agent.objects.filter(agentid=aid).update(agentname=agentname,agentmobileno=agentmobileno,agentemail=agentemail,agentgender=agentgender,agentspealist=agentspealist,agentaddress=agentaddress,agentkycstutas=agentkycstutas,agentstutas=agentstutas)
#         # C.save()
#         return redirect('agent')
#     return render(request,"agent-edit.html",context)
        

      
@login_required(login_url="/login/")
def userregister(request):
    if request.method=="POST":
        username=request.POST.get('uname')
        useremail = request.POST.get('email')
        useraddress = request.POST.get('address')
        userpassword = request.POST.get('pass')
        usermobileno = request.POST.get('mno')
        usergender=request.POST.get('Gender')
        userstutas = True
        print(username)
        # print("arjun")
        # user=User.objects.create(username=username,email=email,password=make_password(password))
        C=Customer(username=username,useremail=useremail,useraddress=useraddress,userpassword=userpassword,usermobileno=usermobileno,usergender=usergender,userstutas=userstutas)
        C.save()
        return redirect('users')
    return render(request,"user-register.html")


@login_required(login_url="/login/")
def agentregister(request):
    if request.method=="POST":
        agentname=request.POST.get('uname')
        agentemail = request.POST.get('email')
        agentmobileno = request.POST.get('mno')
        agentgender = request.POST.get('Gender')
        agentaddress = request.POST.get('address')
        agentspealist=request.POST.get('Specliast')
        agentpassword = request.POST.get('pass')
        agentstutas = True
        agentkycstutas = True
        A=Agent(agentname=agentname,agentemail=agentemail,agentmobileno=agentmobileno,agentgender=agentgender,agentaddress=agentaddress,agentspealist=agentspealist,agentpassword=agentpassword,agentkycstutas=agentkycstutas,agentstutas=agentstutas)
        A.save()
        return redirect('agent')
    return render(request,"./agentregister.html")


@login_required(login_url="/login/")
def addservices(request):
    if request.method=="POST":
        img=request.FILES.get('serviceimg');
        # i=Service(serviceimage=img)
        # i.save()
        servicename = request.POST.get('servicename')
        servicedescription = request.POST.get('servicedescription')
        serviceimage = request.POST.get('serviceimg')
        servicestutas=True
        z=Service(servicename=servicename,servicedescription=servicedescription,serviceimage=img,servicestutas=True)
        z.save()
        return redirect('services')
    return render(request,"add-services.html")

@login_required(login_url="/login/")
def addsubservices(request):
    if request.method=="POST":
        img=request.FILES.get('subserviceimg');
        subservicename = request.POST.get('subservicename')
        subservicedescription=request.POST.get('subservicedescription')
        subserviceprice = request.POST.get('subserviceprice')
        subserviceimage= request.POST.get('subserviceimg')
        serviceid= request.POST.get('serviceid')
        subservicestutas=True
        d=Subservice(serviceid=serviceid,subservicename=subservicename,subservicedescription=subservicedescription,subserviceprice=subserviceprice,subserviceimage=img,subservicestutas=subservicestutas)
        d.save()
        return redirect('subservices')
    allsubservice=Service.objects.all()
    context={'Subservices':allsubservice}
    return render(request,"add-subservices.html",context)
