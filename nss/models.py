# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vpx(models.Model):
    name = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    servicetype = models.CharField(max_length=100)
    curstate = models.CharField(max_length=100)
    effectivestate = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    lbmethod = models.CharField(max_length=100)
    backuplbmethod = models.CharField(max_length=100)
    health = models.CharField(max_length=100)
    totalservices = models.CharField(max_length=100)
    activeservices = models.CharField(max_length=100)
    statechangetimesec = models.CharField(max_length=100)
    fecha_creacion = models.DateField('Fecha de creacción', auto_now=True, auto_now_add=False)
    #class Meta:
        #verbose_name = 'Vpx'
        #verbose_name_plural = 'Vpxs'
    	#ordering = ['name']
    #def __str__(self):
        #return self.name   

class Log(models.Model):
    name = models.CharField(max_length=100)
    name_user = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField('Fecha de creacción', auto_now=True, auto_now_add=False)