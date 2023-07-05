#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones_2 import cargaArchivo, fechaActual, elaboraCartaConcentradoSemanal
from datetime import datetime

#------------------------------------------------------------

hoy = datetime.now()
cadenaFecha = fechaActual(hoy)
archivoInicial = "Bitacora_Fisica_2_NRC_263_Segundo_Parcial_Semana_7.csv"
print()

DF1 = cargaArchivo(archivoInicial)

contadorCartas = 0
contadorNP = 0

Semana =  '7'

for i in DF1.index:
    Estudiante = str(DF1['Estudiante'][i])
    Webinar = str(DF1['Webinar'][i])
    Faltas_Teo = str(DF1['F_Teo'][i])
    Faltas_Lab = str(DF1['F_Lab'][i])
    Previo_Lab = str(DF1['Previo'][i])
    
    #if Estudiante == 'REYES ROBLES NURIA':
    contadorCartas += 1
    print(Estudiante)
    elaboraCartaConcentradoSemanal(Semana, Estudiante, Webinar, Faltas_Teo, Faltas_Lab, Previo_Lab)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))


