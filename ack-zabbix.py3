#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ack-zabbix.py

"""
  Este script é executado automaticamente apos a abertura do ticket no OTRS


  Modificado em 17 de março de 2020
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

from zabbix_api import ZabbixAPI
import sys
 
server = "http://localhost/zabbix"
username = "Admin"             
password = "zabbix"     
 
conexao = ZabbixAPI(server = server)
conexao.login(username, password)

reconhecer_evento = conexao.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no OTRS."})

# Esse código foi publicado originalmete: https://github.com/janssenlima/zabbix-glpi
# e pelo https://www.zabbix.com/forum/em-portugues-y-en-espanol/46365-reconhecer-eventos-e-triggers
