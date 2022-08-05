import email
from email.headerregistry import Address
from pickle import TRUE
from tkinter import FALSE
from django.db import models
from django.contrib.auth.models import User
# from numpy import False_
# from pandas import notnull


# Create your models here
class Customer(models.Model):
    userid=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=200,null=FALSE)
    useremail=models.EmailField(max_length=20,null=FALSE)
    useraddress=models.CharField(max_length=200,null=FALSE)
    userpassword=models.CharField(max_length=30,null=FALSE)
    usermobileno=models.CharField(max_length=10,null=FALSE)
    usergender=models.CharField(max_length=7,null=FALSE)
    userstutas=models.BooleanField(max_length=5)
    
class Agent(models.Model):
    agentid=models.IntegerField(primary_key=True)
    agentname=models.CharField(max_length=30,null=FALSE)
    agentemail=models.EmailField(max_length=20,null=FALSE)
    agentmobileno=models.CharField(max_length=10,null=FALSE)
    agentgender=models.CharField(max_length=5,null=FALSE)
    agentaddress=models.CharField(max_length=200,null=FALSE)
    agentspealist=models.CharField(max_length=200,null=FALSE)
    agentstutas=models.BooleanField(max_length=5,null=FALSE)
    agentkycstutas=models.BooleanField(max_length=5)
    agentpassword=models.CharField(max_length=20,null=FALSE)
    
    
class Kyc(models.Model):
    kycid=models.IntegerField(primary_key=True)
    agentid=models.IntegerField()
    agentaadharno=models.CharField(max_length=12,null=FALSE)
    agentaadharimg=models.ImageField(upload_to='images/',null=FALSE)
    agentbankname=models.CharField(max_length=40,null=FALSE)
    agentifsccode=models.CharField(null=FALSE,max_length=200)
    agentaccountno=models.IntegerField(null=FALSE)
    agentpanno=models.CharField(null=FALSE,max_length=20)
    agentpanimage=models.ImageField(upload_to='images/',null=FALSE)
    agentpassbookimage=models.ImageField(upload_to='images/',null=FALSE)
    agentimage=models.ImageField(upload_to='images/',null=FALSE)
    
    
    
class Service(models.Model):
    serviceid=models.IntegerField(primary_key=True)
    servicename=models.CharField(max_length=20,null=FALSE)
    servicedescription=models.CharField(max_length=20,null=FALSE)
    serviceimage = models.ImageField(upload_to='image/images/')
    servicestutas=models.BooleanField(max_length=5,null=FALSE)
    
    
class Subservice(models.Model):
    subserviceid=models.IntegerField(primary_key=True)
    serviceid=models.IntegerField()
    subservicename=models.CharField(max_length=50,null=FALSE)
    subservicedescription=models.CharField(max_length=20,null=FALSE)
    subserviceimage = models.ImageField(upload_to='image/images/')
    subserviceprice = models.IntegerField()
    subservicestutas=models.BooleanField(max_length=5,null=FALSE)
    
    
class Orderlist(models.Model):
    orderid=models.IntegerField(primary_key=True)
    serviceid=models.IntegerField(null=True,blank=True)
    subserviceid=models.IntegerField(null=True)
    userid=models.IntegerField(null=True)
    agentid=models.IntegerField(null=True,blank=True)
    servicename=models.CharField(max_length=200,null=True)
    orderdatetime=models.DateTimeField(null=True)
    orderotp=models.IntegerField(null=True)
    orderstutas=models.BooleanField(max_length=5,null=True)
    ordercompletetime=models.DateTimeField(null=True,blank=True)
    orderaddress=models.CharField(max_length=200)
    orderprice=models.IntegerField(null=True)
    
class Payment(models.Model):
    paymentid=models.IntegerField(primary_key=True)
    userid=models.IntegerField(null=FALSE)
    orderid=models.IntegerField(null=FALSE)
    amount=models.IntegerField()
    paymentdatetime=models.DateTimeField(null=FALSE)
    paymentstutas=models.BooleanField(max_length=5)
    
class Contactform(models.Model):
    contactid=models.IntegerField(primary_key=True)
    contactname=models.CharField(max_length=200,null=FALSE)
    contactemail=models.EmailField(max_length=30,null=FALSE)
    contactmobileno=models.CharField(max_length=10,null=FALSE)
    contactmessage=models.CharField(max_length=300) 
    
    
class Feedback(models.Model):
    feedbackid=models.IntegerField(primary_key=True)
    userid=models.IntegerField()
    agentid=models.IntegerField()
    feedbackmessage=models.CharField(max_length=300,null=FALSE) 
    feedbackdate=models.DateTimeField(max_length=200,null=FALSE)
