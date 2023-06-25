#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones_2 import cargaArchivo, fechaActual, elaboraCartaConcentrado
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
    Estudiante = str(DF1['Estudiante'][i])
    Webinar = str(DF1['Webinar'][i])
    Personajes = str(DF1['Personajes'][i])
    Densidades = str(DF1['Densidades'][i])
    Conversion = str(DF1['Conversion'][i])
    M_Amb = str(DF1['Medio_Ambiente'][i])
    Ejer_Pascal = str(DF1['Ejer_Pascal'][i])
    Puntos = str(DF1['Puntos'][i])
    Eval_Continua = str(DF1['Eval_Cont'][i])
    Practica_1 = str(DF1['Practica_01'][i])
    Practica_2 = str(DF1['Practica_02'][i])
    Laboratorio = str(DF1['Laboratorio'][i])
    
    if Estudiante == 'REYES ROBLES NURIA':
        contadorCartas += 1
        print(Estudiante)
        elaboraCartaConcentrado(Estudiante, Webinar, Personajes, Densidades, Conversion, M_Amb, Ejer_Pascal, Puntos, Eval_Continua, Practica_1, Practica_2, Laboratorio)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))


