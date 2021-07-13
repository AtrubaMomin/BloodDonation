"""finalmodel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls)
    path('',views.home),
    path('home',views.home),
    path('conque/',views.contactquery,name='contactquery'),
    path('donors/',views.donors,name='donors'),
    #path('adminreg/',views.adminregistration,name='adminregistration'),
    path('register/',views.register,name='register'),
    path('signupcheck/',views.signupcheck,name='signupcheck'),
    path('adminlog/',views.adminlog,name='adminlog'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('logincheck/',views.logincheck,name='logincheck'),
    path('display/',views.display,name='display'),
    path('predform/',views.predform,name='predform'),
    path('predict/',views.predict,name='predict'),
    path('admincheck/',views.admincheck,name='admincheck'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('query/',views.query,name='query'), 
    path('delete/?id=<id>/',views.delete,name= 'delete'),
    path('upddate/',views.update,name = 'update'),
    path('upddatefrm/',views.updatefrm,name = 'updatefrm'),
    path('searchdonar/',views.searchdonar,name = 'searchdonar'),   
    path('infodnr/',views.infodnr,name='infodnr'),
    path('dnrcheck/',views.dnrcheck,name='dnrcheck'),
    path('adddnr/?name=<name>',views.adddnr,name='adddnr'),
    path('dnrform/?name=<name>',views.dnrform,name='dnrform'),
    path('dummydelete/?did=<did>',views.dummydelete,name='dummydelete'),
    path('dummypred/?did=<did>',views.dummypredict,name='dummypred'),
    path("viewdonars/?name=<name>",views.viewdonar,name='viewdonar'),
    path('viewaccptr/?name=<name>',views.viewaccptr,name='viewaccptr'),
    path('accptrsrch/?name=<name>',views.accptrsrch,name='accptrsrch'),
    path('usersearchdonar/',views.usersearchdonar,name = 'usersearchdonar'),
    path('loggddnr/',views.loggddnr,name='loggddnr'),
    path('sample/',views.samplee,name='samplee'),
    path('reg/',views.reg,name='reg'),
    path('seeing/',views.seeing,name='seeing'),
    path('donation/',views.donation,name='donation'),
    path('save/',views.save,name='save'),
    path('allaccptr/?name=<name>',views.allaccptr,name='allaccptr'),
    path('accprofile/?name=<name>',views.accprofile,name='accprofile'),
    path('dnrprofile/?name=<name>',views.dnrprofile,name='dnrprofile'),
    path('accupdate/?name=<name>',views.accupdate,name='accupdate'),
    path('accupdateuser/?name=<name>',views.accupdateuser,name='accupdateuser'),
    path('dnrupdate/?name=<name>',views.dnrupdate,name='dnrupdate'),
    path('dnrupdateuser/?name=<name>',views.dnrupdateuser,name='dnrupdateuser'),
    path('actacc/',views.actacc,name="actacc")
    
    

]

