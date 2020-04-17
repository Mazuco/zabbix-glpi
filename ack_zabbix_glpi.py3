#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# ack_zabbix_glpi.py
## Modificado por: Vitor Mazuco / vitor.mazuco@gmail.com>
## Ultima atualizacao: 12 de fevereiro
## Observacoes: Este script é executado automaticamente apos a abertura do ticket no GLPI

from zabbix_api import ZabbixAPI
import sys
 
server = "http://127.0.0.1/zabbix"
username = "Admin"             
password = "zabbix"     
 
conexao = ZabbixAPI(server = server)
conexao.login(username, password)

reconhecer_evento = conexao.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no GLPI."})

# Esse código foi publicado originalmete pelo 
# https://github.com/janssenlima/zabbix-glpi 
# https://www.zabbix.com/forum/em-portugues-y-en-espanol/46365-reconhecer-eventos-e-triggers
