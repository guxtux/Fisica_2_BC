#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones import cargaArchivo, fechaActual, elaboraEvalRubrica
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
    Paterno = str(DF1['Apellido1'][i])
    Materno = str(DF1['Apellido2'][i])
    Nombre = str(DF1['Nombre'][i])
    Tarea = str(DF1['Tarea'][i])
    Presentacion = str(DF1['Presentación'][i])
    Personajes = str(DF1['Personajes'][i])
    Descripcion = str(DF1['Descripción'][i])
    Relacion = str(DF1['Relación'][i])
    Bibliografia = str(DF1['Bibliografía'][i])
    Ortografia = str(DF1['Ortografía'][i])
    Puntos = str(DF1['Puntos'][i])
    Comentarios = str(DF1['Comentarios'][i])
    
    nombreCompleto = Nombre + ' ' + Paterno + ' ' + Materno

    if Tarea == '1':
        contadorCartas += 1
        print(nombreCompleto)
        elaboraEvalRubrica(nombreCompleto, Presentacion, Personajes, Descripcion, Relacion, Bibliografia, Ortografia, Puntos, Comentarios)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))
