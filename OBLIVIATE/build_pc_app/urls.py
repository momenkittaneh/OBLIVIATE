from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('makeorder',views.makeorder),
    path('confirmorder',views.confirm),
    path('confirm',views.ok),
    path('cart',views.mycart),
    path('details/<int:id>',views.proddetails),
    path('profile',views.myprofile),
    path('addaddress/<int:id>',views.addaddress),
    
]
