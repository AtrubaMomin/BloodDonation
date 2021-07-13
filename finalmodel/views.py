from django.http.response import HttpResponse
from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
import joblib
from finalmodel.models import adminreg
from finalmodel.models import signupuser
from finalmodel.models import login
from finalmodel.models import dnrinfo
from finalmodel.models import tblblooddonars
from finalmodel.models import accptr
from finalmodel.models import admin
from finalmodel.models import tblcontactusquery
from django.contrib import messages


def home(request):
    return render(request,'home.html')

def homeblood(request):
    return render(request,'homeblood.html')

def contactquery(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('ContactNumber') and request.POST.get('EmailId') and request.POST.get('Message'): 
            saverec = tblcontactusquery()
            saverec.name = request.POST.get('name')
            saverec.ContactNumber = request.POST.get('ContactNumber')
            saverec.EmailId = request.POST.get('EmailId')
            saverec.Message = request.POST.get('Message')
            saverec.save()
            messages.success(request,"Message successfully Sent!!!")
        return render(request,'home.html')
    else:
        return(request,'home.html')

def loginuser(request):
    return render(request,'login.html')


def signupcheck(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('bldgrp') and request.POST.get('password') and request.POST.get('cnumber') and request.POST.get('add'): 
            name=request.POST.get('name')
            email = request.POST.get('email')
            pwd = request.POST.get('password')
            cno = request.POST.get('cnumber')
            bldgrp = request.POST.get('bldgrp')
            add = request.POST.get('add')
            print(bldgrp)
            with connection.cursor() as cursor:
                query = "select * from finalmodel_signupuser where uname=%s"
                cursor.execute(query,[name])
                row = cursor.fetchall()
                if row!=1:
                    query = "INSERT INTO `finalmodel_signupuser`(`uname`, `umail`, `pwd`, `uadd`, `cnumber`, `bldgrp`) VALUES (%s,%s,%s,%s,%s,%s)"
                    cursor.execute(query,[name,email,pwd,add,cno,bldgrp])
                    
                    return render(request,'login.html')
                else:
                    print("User Already exist")
                    return render(request,'home.html')
    else:
        return(request,'signup.html')

def adddnr(request,name):
    name =name
    if request.method=='POST': 
        if request.POST.get('rec') and request.POST.get('freq') and request.POST.get('mone') and request.POST.get('fdon'):
            
            rec=request.POST['rec']
            fdon=request.POST['fdon']
            mone=request.POST['mone']
            freq=request.POST['freq']
            with connection.cursor() as cursor:
                query = 'INSERT INTO finalmodel_dnrinfo (`uname`, `recency`, `montary`, `frequency`, `firstdontime`) VALUES (%s,%s, %s, %s, %s);'
                cursor.execute(query,[name,rec,mone,freq,fdon])
                return render(request,'thanks.html',{'name':name})

    else:         
        return render(request,'info_dnr.html')

def logincheck(request):
    if request.method=='POST':
        if request.POST.get('uname') and request.POST.get('pwd'):
            name = request.POST['uname']
            pwd = request.POST['pwd']
            with connection.cursor() as cursor:
                query="Select * from finalmodel_signupuser where uname=%s and pwd=%s"
                cursor.execute(query,[name,pwd])
                row = cursor.fetchall()
                print(len(row))
                if len(row)==1:
                    que = "Select uid from finalmodel_signupuser where uname=%s and pwd =%s"
                    cursor.execute(que,[name,pwd])
                    userid = cursor.fetchone()
                    """ 
                    que = "INSERT INTO loggedin(name) VALUES (%s)"
                    cursor.execute(que,[name])"""
                    return render(request,'loggeddnr.html',{'name':name})
                else:
                    return render(request,'signup.html')
    else:
        return render(request,'signup.html')
    

def register(request):
    return render(request,'signup.html')

def query(request):
    msg = tblcontactusquery.objects.all()
    return render(request,'query.html',{'msg':msg})


def donors(request):
    dnr = tblblooddonars.objects.all()
    return render(request,'donorslist.html',{'dnr':dnr})

def display(request):
    dn = tblblooddonars.objects.all().count()
    print(dn)
    donar = {'dnr':dn}
    return render(request,'dummy.html',donar)

def delete(request ,id):
    userid = id
    print(userid)
    with connection.cursor() as cursor:
        query = "DELETE FROM finalmodel_tblcontactusquery WHERE id = %s"
        cursor.execute(query,[userid])
        return redirect('/query/')
    


def predform(request):
    return render(request,'predict.html')
    


def adminlog(request):
    return render(request,'adminlog.html')

def actacc(request):
    accps = accptr.objects.all()
    return render(request,'accpt.html',{'accps':accps})

def admincheck(request):
    if request.method=='POST':
        if request.POST.get('uname') and request.POST.get('pwd'):
            name = request.POST['uname']
            print(name)
            pwd = request.POST['pwd']
            print(pwd)
           
            with connection.cursor() as cursor:
                query = "Select * from finalmodel_admin where UserName = %s and Password = %s"
                cursor.execute(query,[name,pwd])
                row = cursor.fetchall()
                print(len(row))
                if len(row)!= 0:
                    acccnt = accptr.objects.all().count()
                    msg = tblcontactusquery.objects.all().count()
                    acc = accptr.objects.all().count()
                    user = signupuser.objects.all().count()
                    actdnr = dnrinfo.objects.all().count()
                    print(actdnr)
                    admdict = {'acccnt':acccnt, 'msg':msg,'acc':acc,'user':user,'actdnr':actdnr}
                    
                    return render(request,'dashboard.html',admdict) 
                else:
                    return render(request,'home.html')

def adminhome(request):
    acccnt = accptr.objects.all().count()
    msg = tblcontactusquery.objects.all().count()
    acc = accptr.objects.all().count()
    user = signupuser.objects.all().count()
    actdnr = dnrinfo.objects.all().count()
    print(actdnr)
    admdict = {'acccnt':acccnt , 'msg':msg,'acc':acc,'user':user,'actdnr':actdnr}
    
    return render(request,'dashboard.html',admdict) 

def update(request):
    return render(request,'updateform.html')

def updatefrm(request):
    if request.method=='POST':
        if request.POST.get('uname') and request.POST.get('pwd'):
            name = request.POST['uname']
            pwd = request.POST['pwd']
            with connection.cursor() as cursor:
                query = ' INSERT INTO `finalmodel_admin`(`UserName`, `Password`) VALUES (%s, %s);'
                cursor.execute(query,[name,pwd])
                acccnt = accptr.objects.all().count()
                msg = tblcontactusquery.objects.all().count()
                acc = accptr.objects.all().count()
                user = signupuser.objects.all().count()
                actdnr = dnrinfo.objects.all().count()
                admdict = {'acccnt':acccnt , 'msg':msg,'acc':acc,'user':user,'actdnr':actdnr}
               # print(dnr)
                return render(request,'dashboard.html',admdict) 
                
    


def searchdonar(request):
    if request.method=='POST':
        if request.POST.get('srchbldgrp'):
            bldgrp = request.POST['srchbldgrp']
            print(bldgrp)
            dnrs =tblblooddonars.objects.filter(bloodgroup = bldgrp)
            #users = tblblooddonars.objects.filter(Name == name).count()
            #dnrs={'users':users}
            #print(users)

            return render(request,'srchdnr.html',{'dnrs':dnrs})

def usersearchdonar(request):
    if request.method=='POST':
        if request.POST.get('srchbldgrp'):
            bldgrp = request.POST['srchbldgrp']
            print(bldgrp)
            dnrs =tblblooddonars.objects.filter(bloodgroup = bldgrp)
            return render(request,'usersrchdnr.html',{'dnrs':dnrs})

def infodnr(request):
    return render(request,'info_dnr.html')

def dnrcheck(request):
    return render(request,'info_dnr.html')

def predict(request):
    pred = dnrinfo.objects.all()
    return render (request,'dummy1.html',{'pred':pred})

def dummydelete(request,did):
    userid = did
    with connection.cursor() as cursor:
        query = "DELETE FROM finalmodel_dnrinfo WHERE did = %s"
        cursor.execute(query,[userid])
        pred = dnrinfo.objects.all()
        return render (request,'dummy1.html',{'pred':pred})

def dummypredict(request,did):
    userid = did
    print(userid)
    with connection.cursor() as cursor:
        query = "select * from finalmodel_dnrinfo where did=%s"
        cursor.execute(query,[userid])
        kNN=joblib.load('finalmodel.sav')
        #pred = dnrinfo.objects.all()  
        row = cursor.fetchone()
        name=row[1]
        li=[]
        li.append(row[2])
        li.append(row[3])
        li.append(row[4])
        li.append(row[5])
            #print(li,end=" ")
        ans=kNN.predict([li])
        #print(ans)
        quer1 = "select * from finalmodel_signupuser where uname = %s" 
        cursor.execute(quer1,[name])
        row = cursor.fetchone()
        print(row)
        
        email = row[2]
        Location = row[4]
        bloodgrp = row[6]
        #print(name)
        #print(email)
        #print(Location)
        #print(bloodgrp)

    return render(request,'dummy2.html',{'name':name,'email':email,'Location':Location,'bloodgrp':bloodgrp,'ans':ans})


def viewdonar(request,name):
    uname = name
    print(uname)
    dnr = tblblooddonars.objects.all()
    dnrcnt = tblblooddonars.objects.all().count()
    return render(request,'alldonar.html',{'dnr':dnr,'dnrcnt':dnrcnt})
    

def viewaccptr(request,name):
    uname = name
    with connection.cursor() as cursor:
        quer1 = "SELECT * FROM `finalmodel_signupuser` WHERE uname = %s"
        cursor.execute(quer1,[uname])
        row1 = cursor.fetchone()
        #print(row1)
        mail = row1[2]
        Location = row1[4]
        bloodgrp = row1[6]
        contact = row1[5]
        print(mail)
        print(Location)
        print(contact)
        quer2 = "INSERT INTO `finalmodel_accptr`(`name`, `bldgrp`, `location`, `contact`) VALUES (%s,%s,%s,%s)"
        cursor.execute(quer2,[uname,bloodgrp,Location,contact])

        #acptrs = {'name':name,'mail':mail,'Location':Location,'bloodgrp':bloodgrp,'contact':contact}

        return render(request,'accptrthanks.html',{'name':name})

def loggddnr(request):
    return render(request,'loggeddnr.html')

def samplee(request):
    return render(request,'samplee.html')

def seeing(request):
    return render(request,'seeing.html')
def save(request):
    return render(request,'save.html')
def donation(request):
    return render(request,'donate.html')
def reg(request):
    return render(request,'reg.html')
def dnrform(request,name):
    name=name
    return render(request,'dnrform.html',{'name':name})


def allaccptr(request,name):
    name=name
    with connection.cursor() as cursor:
        quer1 = "SELECT * FROM `finalmodel_signupuser` WHERE uname = %s"
        cursor.execute(quer1,[name])
        row1 = cursor.fetchone()
        bloodgrp = row1[6]
        dnrs =accptr.objects.filter(bldgrp = bloodgrp)
        return render(request,'allaccptr.html',{'dnrs':dnrs,'name':name})

def dnrprofile(request,name):
    name=name
    with connection.cursor() as cursor:
        quer1 = "SELECT * FROM `finalmodel_signupuser` WHERE uname = %s"
        cursor.execute(quer1,[name])
        row = cursor.fetchone()
        mail = row[2]
        Location = row[4]
        bloodgrp = row[6]
        contact = row[5]
        return render(request,'dnrprofile.html',{'name':name,'mail':mail,'Location':Location,'bloodgrp':bloodgrp,'contact':contact})
def accprofile(request,name):
    name=name
    with connection.cursor() as cursor:
        quer1 = "SELECT * FROM `finalmodel_signupuser` WHERE uname = %s"
        cursor.execute(quer1,[name])
        row = cursor.fetchone()
        mail = row[2]
        Location = row[4]
        bloodgrp = row[6]
        contact = row[5]
        return render(request,'accprofile.html',{'name':name,'mail':mail,'Location':Location,'bloodgrp':bloodgrp,'contact':contact})


def accupdate(request,name):
    name=name
    return render(request,'accupdatefrm.html',{'name':name})

def accupdateuser(request,name):
    name=name
    if request.method=='POST':
        if request.POST.get('loc') and request.POST.get('contact') and request.POST.get('pwd') and request.POST.get('mail'):
            Location = request.POST['loc']
            contact = request.POST['contact']
            pwd = request.POST['pwd']
            mail = request.POST['mail']
            with connection.cursor() as cursor:
                query = "UPDATE `finalmodel_signupuser` SET `umail`=%s,`pwd`=%s,`uadd`=%s,`cnumber`=%s WHERE uname = %s"
                cursor.execute(query,[mail,pwd,Location,contact,name])
                quer1 = "SELECT * FROM `finalmodel_signupuser` WHERE uname = %s"
                cursor.execute(quer1,[name])
                row1 = cursor.fetchone()
                bloodgrp = row1[6]
                
                return render(request,'accprofile.html',{'bloodgrp':bloodgrp,'name':name,'contact':contact,'mail':mail,'Location':Location})

def dnrupdate(request,name):
    name=name
    return render(request,'dnrupdatefrm.html',{'name':name})

def accptrsrch(request,name):
    name = name
    with connection.cursor() as cursor:
        quer1 = "SELECT * FROM `finalmodel_signupuser` WHERE uname = %s"
        cursor.execute(quer1,[name])
        row1 = cursor.fetchone()
        bloodgrp = row1[6]
        dnrs =tblblooddonars.objects.filter(bloodgroup = bloodgrp)
        return render(request,'accptrsrch.html',{'dnrs':dnrs,'name':name})

def dnrupdateuser(request,name):
    name=name
    if request.method=='POST':
        if request.POST.get('loc') and request.POST.get('contact') and request.POST.get('pwd') and request.POST.get('mail'):
            Location = request.POST['loc']
            contact = request.POST['contact']
            pwd = request.POST['pwd']
            mail = request.POST['mail']
            with connection.cursor() as cursor:
                query = "UPDATE `finalmodel_signupuser` SET `umail`=%s,`pwd`=%s,`uadd`=%s,`cnumber`=%s WHERE uname = %s"
                cursor.execute(query,[mail,pwd,Location,contact,name])
                quer1 = "SELECT * FROM `finalmodel_signupuser` WHERE uname = %s"
                cursor.execute(quer1,[name])
                row1 = cursor.fetchone()
                bloodgrp = row1[6]
                
                return render(request,'dnrprofile.html',{'bloodgrp':bloodgrp,'name':name,'contact':contact,'mail':mail,'Location':Location})



