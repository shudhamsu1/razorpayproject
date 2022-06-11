from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    
    path("", views.home, name="home"),
    # path("first/",views.firstPage,  name="firstPage"),
    path("contact/",views.contactus,  name="contactus"),
    path("product/",views.product,  name="product"),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
    path("startPay/",views.startPay,  name="startPay"),
    
]