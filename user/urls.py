"""allinone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include

from user import views
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('term-conditions/',views.tc,name="tc"),
    path('about-us/',views.about,name="about"),
    path('contect-us/',views.contect,name="contect"),
    path('register-type/',views.registert,name="registert"),
    path('uagentregister/',views.signup_agent,name="uagentregister"),
    path('login/',views.login_user,name="login"),
    path('adminpan/',views.login_user,name="adminpan"),
    path('customerdash/',views.customerdash,name="customerdash"),
    # path('coustomer/',views.coustomer,name="coustomer"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="user/forget-password.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="user/mailsent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="user/changepassword.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="user/gotologin.html"),name="password_reset_complete"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.user_logout,name="logout"),
    path('services/',views.serviceuser,name="serviceuser"),
    path('electricians/<int:id>/',views.electricians,name="electricians"),
    path('homepainting/',views.homepainting,name="homepainting"),
    path('carpanter/',views.carpanter,name="carpanter"),
    path('plumber/',views.plumber,name="plumber"),
    # path('password_reset/',views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset password"),

    path('bookele/',views.bookele,name="bookele"),
    
    path('cbookele/<int:id>/',views.cbookele,name="cbookele"),
    path('ccarpanter/',views.ccarpanter,name="ccarpanter"),
    path('celectricians/<int:id>/',views.celectricians,name="celectricians"),
    path('chomepainting/',views.chomepainting,name="chomepainting"),
    path('cplumber/',views.cplumber,name="cplumber"),
    path('mybooking/',views.mybooking,name="mybooking"),
    path('transaction/',views.transaction,name="transaction"),
    path('fedback/',views.fedback,name="fedback"),
    path('notification/',views.notification,name="notification"),
    path('bookingongoing/',views.bookingongoing,name="bookingongoing"),
    path('bookinghistory/',views.bookinghistory,name="bookinghistory"),
    path('viewbooking/<int:id>/',views.viewbooking,name="viewbooking"),
    path('profileedit/',views.profileedit,name="profileedit"),
    path('profile/',views.profile,name="profile"),

# agent
    path('agentindex/',views.agentindex,name="agentindex"),
    path('agentprofile/',views.agentprofile,name="agentprofile"),
    path('agentpayment/',views.agentpayment,name="agentpayment"),
    path('agentorderlist/',views.agentorderlist,name="agentorderlist"),
    path('agentnotification/',views.agentnotification,name="agentnotification"),
    path('agentkycdetail/',views.agentkycdetail,name="agentkycdetail"),
    path('agentedits/',views.agentedits,name="agentedits"),
    path('insertorder/',views.insertorder,name="insertorder"),
    path('vieworderdetail/',views.vieworderdetail,name="vieworderdetail"),
    path('viewnotificationdetails/<int:id>/',views.viewnotificationdetails,name="viewnotificationdetails"),
    path('orderaccept/<int:id>/',views.orderaccept,name="orderaccept"),


]