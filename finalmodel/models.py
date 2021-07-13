from django.db import models


class tblcontactusquery(models.Model):
    id = models.AutoField(primary_key = True) 
    name = models.CharField(max_length=100)
    ContactNumber = models.CharField(max_length=100)
    EmailId = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)
    class meta:
        db_table = 'tblcontactusquery'

class signupuser(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100)
    umail = models.CharField(max_length=100)
    pwd = models.CharField(('password'),max_length=100)
    uadd = models.CharField(max_length=100)
    cnumber = models.CharField(max_length=100)
    bldgrp = models.CharField(max_length=100)
    class meta:
        db_table="signupuser"

class adminreg(models.Model):
    adname = models.CharField(max_length=100)
    prevpwd = models.CharField(('password'),max_length=100)
    npwd = models.CharField(('password'),max_length=100)
    class meta:
        db_table="adminreg"

class login(models.Model):
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    class meta:
        db_table = "login"

class tblblooddonars(models.Model):
    Name = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    class meta:
        db_table = "tblblooddonars"

class dnrinfo(models.Model):
    did = models.AutoField(primary_key = True) 
    uname = models.CharField(max_length=100)
    recency = models.CharField(max_length=100)
    montary = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    firstdontime = models.CharField(max_length=100)
    class meta:
        db_table = "dnfinfo"


class accptr(models.Model):
    aid = models.AutoField(primary_key = True) 
    
    name = models.CharField(max_length=100)
    bldgrp = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    class meta:
        db_table = "accptr"

class admin(models.Model):
    adid = models.AutoField(primary_key = True)
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    class meta:
        db_table = "admin"


