#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  HostJack-Chekcer by Neo-Jack Ene/2020 #
import socket 
import socks 
import requests 
import time 
import sys 
import colorama 
from colorama import Fore, Back, Style 

port = str(443) 
puerto = str(80)
reintentar = int(99999)
retrasar = int(5)
timeout = int(10)
http = "http://"
https = "https://"
tor_args = 'NADA'

def Funciones():
    print(Fore.RED + Style.BRIGHT + "...." + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Menu de Ayuda " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "...." + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + " HostJack-Checker corre con Python 3.6.9\n Confirma tu version the python con: python3 -V\n " + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + " Modo de usar:" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Sin TOR" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "   <" + Style.RESET_ALL + Style.BRIGHT + " python3 hostjack.py www.ejemplo.com " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "> \n" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "          <" + Style.RESET_ALL + Style.BRIGHT + " python3 hostjack.py3 www.ejemplo.com -F " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "> \n" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Con TOR" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "   <" + Style.RESET_ALL + Style.BRIGHT + " python3 hostjack.py www.ejemplo.com -T " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "> " + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Este Menu" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " <" + Style.RESET_ALL + Style.BRIGHT + " python3 hostjack.py -h " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "> " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "-h, --help o --ayuda" + Style.RESET_ALL)
    print("")

if len(sys.argv) >= 2:
  try:
      tor_args = sys.argv[2]
      if tor_args == "-T":
        tor = True
      if not tor_args == "-T":
        tor_args = "-F"
        tor = False
  except:      
      tor_args = "-F"
      tor = False

if len(sys.argv) > 1:
    web = sys.argv[1]
else:
    web = "-h"

if web == "-h":
    Funciones()
    sys.exit(0)
if web == "--help":
    Funciones()
    sys.exit(0)
if web == "--ayuda":
    Funciones()
    sys.exit(0)

if tor is True:
    ipcheck_url = 'http://canihazip.com/s' 
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050) 
    socket.socket = socks.socksocket
    try:
        tor_ip = requests.get(ipcheck_url) 
        tor_ip = str(tor_ip.text) 
    except requests.exceptions.RequestException as e:
        sys.exit(0)

if tor is False: 
    ipcheck_url2 = 'http://canihazip.com/s' 
    try: 
        regular_ip = requests.get(ipcheck_url2) 
        regular_ip = str(regular_ip.text) 
    except requests.exceptions.RequestException as e:
        sys.exit(0)

print(Fore.BLUE + Style.BRIGHT + "............................." + Style.RESET_ALL)
print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Iniciando... HostJack-Checker" + Style.RESET_ALL)
print(Fore.GREEN + Style.BRIGHT + "Para Salir..." + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " Ctlr + Z" + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT + "............................." + Style.RESET_ALL)

if tor is True:
    print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Comprobando su Informacion IP ..." + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Conexion TOR: " + Style.RESET_ALL + Back.GREEN + "Activada" + Style.RESET_ALL)
    try:
        print(Fore.GREEN + Style.BRIGHT + "Nueva Conexion IP-TOR: "+ Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + tor_ip + Style.RESET_ALL)       
    except requests.exceptions.RequestException as e:
            sys.exit(0)

if tor is False:
    print(Back.CYAN + Fore.YELLOW + Style.BRIGHT + "Comprobando su Informacion IP ..." + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "Conexion TOR: " + Style.RESET_ALL + Back.RED + "Desactivado"+ Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " o " + Style.RESET_ALL + Back.RED + "NO Encontrada" + Style.RESET_ALL)
    ipcheck_url2 = 'http://canihazip.com/s' 
    try:
        regular_ip = requests.get(ipcheck_url2) 
        regular_ip = str(regular_ip.text)
        print(Fore.GREEN + Style.BRIGHT + "Tu IP Externa es: "+ Style.RESET_ALL + Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + regular_ip + Style.RESET_ALL)        
        time.sleep(3)
    except requests.exceptions.RequestException as e:
            sys.exit(0)

def isOpen443(web, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((web, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True 
        except socket.timeout as e: 
                print("")
                print(Fore.GREEN + Style.BRIGHT + "Host: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + https + web + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " (" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + port + Style.RESET_ALL + Fore.RED + Style.BRIGHT + ") " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "\n -->  Estado: " + Style.RESET_ALL + Fore.WITE + Style.BRIGHT + " Error 504" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " (TimeOut)" + Style.RESET_ALL) 
                print(Fore.GREEN + Style.BRIGHT + "Verificicando ... " + Style.RESET_ALL)
                return False
        except:
                return False
        finally:
                s.close()

def isOpen80(web, puerto):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((web, int(puerto)))
                s.shutdown(socket.SHUT_RDWR)
                return True 
        except socket.timeout as e: 
                print("")
                print(Fore.GREEN + Style.BRIGHT + "Host: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + https + web + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " (" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + puerto + Style.RESET_ALL + Fore.RED + Style.BRIGHT + ") " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "\n -->  Estado: " + Style.RESET_ALL + Fore.WITE + Style.BRIGHT + " Error 504" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " (TimeOut)" + Style.RESET_ALL)  
                print(Fore.GREEN + Style.BRIGHT + "Verificicando ... " + Style.RESET_ALL)
                return False
        except:
                return False
        finally:
                s.close()

def checkHost(web, port, puerto):
        estado = False 
        if tor is True:  
             tor_status = Fore.GREEN + Style.BRIGHT + "Con Tor " + Style.RESET_ALL
        else:
             tor_status =  Fore.RED + Style.BRIGHT + "Sin Tor " + Style.RESET_ALL
        for i in range(reintentar):
                print(Back.MAGENTA + Fore.YELLOW + Style.BRIGHT + "Revisando Puertos: 80 y 443" + Style.RESET_ALL)
                if isOpen80(web, puerto):                        
                        estado = True
                        time.sleep(retrasar)
                        print("")
                        print(Fore.GREEN + Style.BRIGHT + "Conectado: " + Style.RESET_ALL + tor_status) 
                        print(Fore.GREEN + Style.BRIGHT + "Host: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + http + web + Fore.GREEN + Style.BRIGHT + " (" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + puerto + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ") " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "\n -->  Estado: " + Style.RESET_ALL + Back.GREEN + Style.BRIGHT + " Operando " + Style.RESET_ALL)
                        print(Fore.GREEN + Style.BRIGHT + "Verificicando ... " + Style.RESET_ALL)
                else:
                        time.sleep(retrasar)
                        print("")
                        print(Fore.GREEN + Style.BRIGHT + "Conectado: " + Style.RESET_ALL + tor_status) 
                        print(Fore.GREEN + Style.BRIGHT + "Host: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + http + web + Fore.RED + Style.BRIGHT + " (" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + puerto + Style.RESET_ALL + Fore.RED + Style.BRIGHT + ") " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "\n -->  Estado: " + Style.RESET_ALL + Back.RED + Style.BRIGHT + " No Disponible " + Style.RESET_ALL)
                        print(Fore.GREEN + Style.BRIGHT + "Verificicando ... " + Style.RESET_ALL)
                if isOpen443(web, port):                        
                        estado = True
                        time.sleep(retrasar)
                        print("")
                        print(Fore.GREEN + Style.BRIGHT + "Conectado: " + Style.RESET_ALL + tor_status) 
                        print(Fore.GREEN + Style.BRIGHT + "Host: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + https + web + Fore.GREEN + Style.BRIGHT + " (" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + port + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ") " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "\n -->  Estado: " + Style.RESET_ALL + Back.GREEN + Style.BRIGHT + " Operando " + Style.RESET_ALL)
                        print(Fore.GREEN + Style.BRIGHT + "Verificicando ... " + Style.RESET_ALL)
                else:
                        time.sleep(retrasar)
                        print("")
                        print(Fore.GREEN + Style.BRIGHT + "Conectado: " + Style.RESET_ALL + tor_status) 
                        print(Fore.GREEN + Style.BRIGHT + "Host: " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + https + web + Fore.RED + Style.BRIGHT + " (" + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + port + Style.RESET_ALL + Fore.RED + Style.BRIGHT + ") " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + "\n -->  Estado: " + Style.RESET_ALL + Back.RED + Style.BRIGHT + " No Disponible " + Style.RESET_ALL)
                        print(Fore.GREEN + Style.BRIGHT + "Verificicando ... " + Style.RESET_ALL)

        return estado

checkHost(web, puerto, port)

