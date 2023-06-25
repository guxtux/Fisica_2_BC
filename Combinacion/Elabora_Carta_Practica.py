#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones import cargaArchivo, fechaActual, elaboraCartaPractica
from datetime import datetime

#------------------------------------------------------------

hoy = datetime.now()
cadenaFecha = fechaActual(hoy)
archivoInicial = input("Ingresa el nombre del archivo .csv: ")
print()

DF1 = cargaArchivo(archivoInicial)

contadorCartas = 0
contadorNP = 0

for i in DF1.index:
    Practica = str(DF1['Practica'][i])
    Entregada = str(DF1['Entregada'][i])
    Estudiante = str(DF1['Estudiante'][i])
    Preparacion = str(DF1['Preparacion'][i])
    T_Experimental = str(DF1['T_Experimental'][i])
    Participacion = str(DF1['Participacion'][i])
    Reporte = str(DF1['Reporte'][i])
    Conclusiones = str(DF1['Conclusiones'][i])
    Calificacion = str(DF1['Calificacion'][i])
    Comentarios = str(DF1['Comentarios'][i])

    if int(Entregada) == 1:
        if Estudiante == 'VELAZQUEZ RAMIREZ FERNANDO DANIEL':
            contadorCartas += 1
            print(Estudiante)

            elaboraCartaPractica(Practica, Estudiante, Preparacion, T_Experimental, Participacion, Reporte, Conclusiones, Calificacion, Comentarios)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))
