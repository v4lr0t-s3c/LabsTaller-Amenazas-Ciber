from __future__ import print_function
from collections import OrderedDict
from importlib import import_module
import os
from datetime import date, datetime
import time
os.system("clear")

def Investigacion():
    archivo = open('/var/lib/tor/cached-microdesc-consensus')
    w = 0
    diccionario = {}
    for linea in archivo:
        linea = linea.rstrip()

        if linea.startswith("r "):
            lineaR = linea.split(' ')
            direccionip = lineaR[5]

        if linea.startswith("w "):
            w = w + 1
            LineaW = linea.replace('w Bandwidth=', '')
            Velocidad = LineaW.split(' ')
            diccionario[direccionip] = int(Velocidad[0])

    NodosPorVelocidad = OrderedDict(sorted(diccionario.items(),key=lambda x:x[1], reverse=True))
    n = 0

    result_inv = []
    for ip in enumerate(NodosPorVelocidad):
        if n == 10:
            break
        ip_dir = ip[1]
        velc = diccionario[ip[1]]
        result_ip = f"{ip_dir:20} :{velc}\n"
        result_inv.append(result_ip)
        n +=1

    result = {
        'IPs': result_inv,
        'Nodos': w
    }
    archivo.close()
    return result

def EscribirArchivo(result):

    ips = result['IPs']
    nodos = result['Nodos']
    now = str(datetime.now())[:19]
    titulo = f"Inicio: {now} - Nodos: {nodos}\n"
    archivo_investigacion.write(titulo)
    for ip in ips:
        archivo_investigacion.write(ip)
    archivo_investigacion.write('------------------------------------------------------\n')

if __name__ == '__main__':
    try:
        archivo_investigacion = open('investigacion.txt', 'a')
        hora = time.ctime()
        print(f"Lectura:{i+1} - Fecha:{datetime.now()}")
        result = Investigacion()
        EscribirArchivo(result)
        archivo_investigacion.close()
    except Exception as e:
        print(f"Error: {e}")
