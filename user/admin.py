from django.contrib import admin

# from mca.allinone.adminpan.views import category

# from mca.allinone.adminpan.views import category
from .models import Customer, Service,Kyc,Subservice,Orderlist,Payment,Contactform,Feedback,Agent

# Register your models here.

class customerAdmin(admin.ModelAdmin):
    list_display=('userid','username','useremail','useraddress','userpassword','usermobileno','usergender','userstutas','userpassword')
    
class agentAdmin(admin.ModelAdmin):
    list_display=('agentid','agentname','agentemail','agentmobileno','agentgender','agentaddress','agentspealist','agentstutas','agentkycstutas','agentpassword')
  
class kycAdmin(admin.ModelAdmin):
    list_display=('kycid','agentid','agentaadharno','agentaadharimg','agentbankname','agentifsccode','agentaccountno','agentpanno','agentpanimage','agentpassbookimage','agentimage')
      
class serviceAdmin(admin.ModelAdmin):
    list_display=('serviceid','servicename','serviceimage','servicestutas')
    
class subserviceAdmin(admin.ModelAdmin):
    list_display=('subserviceid','serviceid','subservicename','subserviceimage','subserviceprice','subservicestutas')
    
class orderlisteAdmin(admin.ModelAdmin):
    list_display=('orderid','serviceid','subserviceid','userid','agentid','servicename','orderdatetime','orderotp','orderstutas','ordercompletetime','orderaddress','orderprice')
    
class paymentAdmin(admin.ModelAdmin):
    list_display=('paymentid','userid','orderid','amount','paymentdatetime','paymentstutas') 
    
    
class contactformAdmin(admin.ModelAdmin):
    list_display=('contactid','contactname','contactemail','contactmobileno','contactmessage')
    
class feedbackAdmin(admin.ModelAdmin):
    list_display=('feedbackid','userid','agentid','feedbackmessage','feedbackmessage','feedbackdate')

    
admin.site.register(Customer,customerAdmin) 
admin.site.register(Agent,agentAdmin)
admin.site.register(Service,serviceAdmin)
admin.site.register(Subservice,subserviceAdmin)
admin.site.register(Orderlist,orderlisteAdmin)
admin.site.register(Payment,paymentAdmin)
admin.site.register(Contactform,contactformAdmin)
admin.site.register(Feedback,feedbackAdmin)
admin.site.register(Kyc,kycAdmin)




