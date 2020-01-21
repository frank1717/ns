# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Vpx,Log

admin.site.register(Vpx)

admin.site.register(Log)
#@admin.register(Log)
# class LogAdmin(admin.ModelAdmin):
#     list_display = ('name_vip', 'name_user', 'creation_date','action')
# Register your models here.
