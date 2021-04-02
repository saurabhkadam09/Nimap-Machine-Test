
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage),
    path('userlogin',views.userlogin),
    path('logout',views.logout),
    path('addclient',views.addclient),
    path('viewclient',views.viewclient),
    path('editclient/<id>',views.editclient),
    path('deleteclient/<id>',views.deleteclient),
    path('addproject',views.addproject),
    path('assignuser',views.assignuser),
    path('myprojects',views.myprojects),
]
