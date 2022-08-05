from django.urls import path
from adminpan import views
urlpatterns = [
    # path('',views.home,name="home"),
    path('adminpan/',views.adminpan,name='adminpan'),
    path('agent/',views.agent,name='agent'),
    path('order-list/',views.order,name='order'),
    path('services/',views.services,name='services'),
    path('subservices/',views.subservices,name='subservices'),
    path('users/',views.users,name='users'),
    
    path('payment/',views.payment,name='payment'),
    path('contectus/',views.contectus,name='contectus'),
    path('setting/',views.setting,name='setting'),
    path('useredit/<int:id>/',views.useredit,name='useredit'),
    path('agentedit/<int:id>/',views.agentedit,name='agentedit'),
    path('subservicesedit/<int:id>/',views.subservicesedit,name='subservicesedit'),
    path('agentregister/',views.agentregister,name="agentregister"),
    path('addsubservices/',views.addsubservices,name="addsubservices"),
    path('servicesedit/<int:id>/',views.servicesedit,name="Servicesedit"),
    path('addservices/',views.addservices,name="addservices"),
    path('feedback/',views.feedback,name='feedback'),
    
    path('deletec/<int:id>/',views.delete_data_customer,name='deletedatac'),
    path('delete/<int:id>/',views.delete_data_agent,name='deletedataagent'),
    path('deleteo/<int:id>/',views.delete_data_orderlist,name='deletedataorderlist'),
    path('deletep/<int:id>/',views.delete_data_payment,name='deletedatapayment'),
    path('deletecc/<int:id>/',views.delete_data_contact,name='deletedatacontact'),
    path('deletek/<int:id>/',views.delete_data_kyc,name='deletedatakyc'),
    path('deletef/<int:id>/',views.delete_data_feedback,name='deletedatafeedback'),
    path('deleteser/<int:id>/',views.delete_data_service,name='deletedataservice'),
    path('deletesub/<int:id>/',views.delete_data_subservice,name='deletedatasubservice'),
    # path('userdata/',views.staff,name='userdata'),
    
    
    # path('deletea/<int:id>/',views.delete_data_area,name='deletedataarea'),
    # path('deletecat/<int:id>/',views.delete_data_category,name='deletedatacategory'),
    # path('deletecatee/<int:id>/',views.delete_data_subservices,name='deletedatasubcategory'),
    
    path('userregister/',views.userregister,name="userregister"),

    path('agentkyc/',views.agentkyc,name="agentkyc"),
    
    path('updatedatacustomer/',views.update_data_customer,name='userupdate'),
    path('updatedataagent/',views.update_data_user,name='agentupdate'),
    path('updatedatasubservice/',views.update_data_subservice,name='subserviceupdate'),
    path('updatedataservice/',views.update_data_service,name='serviceupdate'),
    
]
