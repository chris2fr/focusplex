from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='I')[0]

class Who(models.Model):
    name = models.CharField(max_length=255)
    do_does = models.CharField(max_length=16,default="do")
    django_user = null
    notes = models.TextField
    email = models.CharField(max_length=128)
    tel = models.CharField(max_length=128)
    
class WhatEtc(models.Model):
    to = models.CharField(max_length=255)
    who = models.ForeignKey(Who,on_delete=models.SET(get_sentinel_user))
    do = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    whom = models.ForeignKey(Who,on_delete=models.SET_NULL,blank=True,null=True)
    etc = models.TextField()