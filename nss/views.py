# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Log
import requests
import socks
import socket
import json
import time
from datetime import datetime
# Create your views here.
# def reinicio(request,id_reinicio):
#        #ip = 'localhost'  # change your proxy's ip
#    #port = 22  # change your proxy's port
#    #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
#    #socket.socket = socks.socksocket
#    #dictionario = {"id_reinicio": id_reinicio}
#    #print (dictionario)
#    print 'Ale'
#    return render(request, 'vip/respuesta.html')
# def reinicio2(request,id_reinicio):
#    #ip = 'localhost'  # change your proxy's ip
#    #port = 22  # change your proxy's port
#    #socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
#    #socket.socket = socks.socksocket
#    #dictionario = {"id_reinicio": id_reinicio}
#    #print (dictionario)
#    print 'Ale'
#    return render(request, 'vip/respuesta.html')
def vip(request):
    IP = "192.168.33.70"
    URL = "http://" + IP + "/nitro/v1/config/"
    URL_LBVSERVER = URL + 'lbvserver'
    URL_SERVER = URL + 'server'
    URL_SERVICE = URL + 'service'
    URL_SERVICEGROUP = URL + 'servicegroup'
    URL_SERVERBINDING = URL + 'server_binding/'
    URL_SERVICEBINDING = URL + 'svcbindings/'
    AUTHORIZATION = "Basic QzE5ODIzOiRIdW50ZXIyMDIw"
    #logs = Log.objects.all()
    #context = {'logs': logs}
    ip = 'localhost'  # change your proxy's ip
    port = 22  # change your proxy's port
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
    socket.socket = socks.socksocket
    headers = {'Content-Type': 'application/vnd.com.citrix.netscaler.lbvserver+json', 'Authorization': AUTHORIZATION,
               'timeout': '12000'}
    res = requests.get(URL_LBVSERVER, headers=headers)
    #print(res2)
    res2 = json.loads(res.text)
    lbvserver2 = res2["lbvserver"]
    # print("res22" + str(lbvserver2))
    dictionario = {"lbvserver2": lbvserver2}
    #print 'hola'
    #print(dictionario)
    return render(request, 'vip/vip.html', dictionario)
def reinicio(request,id_reinicio,id_user):
   IP = "192.168.33.70"
   URL = "http://" + IP + "/nitro/v1/config/"
   virtual_server_conf = "lbvserver"
   enable_action = "?action=enable"
   disable_action = "?action=disable"
   URL_ENABLE_VSERVER = URL + virtual_server_conf + enable_action
   URL_DISABLE_VSERVER = URL + virtual_server_conf + disable_action
   AUTHORIZATION = "Basic QzE5ODIzOiRIdW50ZXIyMDIw"
   payload = {"lbvserver": {"name": id_reinicio}}
   headers = {'Content-Type': 'application/vnd.com.citrix.netscaler.lbvserver+json',
              'Authorization': AUTHORIZATION}
   response2 = requests.post(URL_DISABLE_VSERVER, data=json.dumps(payload), headers=headers)
   
   if response2.status_code == 200:
        print 'disable correcto'
   time.sleep(7)
   response3 = requests.post(URL_ENABLE_VSERVER, data=json.dumps(payload), headers=headers)
   if response3.status_code == 200:
        print 'enable correcto'
   else:
        print 'fallo reinicio'
   name_vip2 = {'id_reinicio': id_reinicio}
   l = Log(name_vip = id_reinicio , name_user=id_user,action='reinicio')
   l.save()
   print(name_vip2)
   return render(request, 'vip/respuesta.html',name_vip2)
