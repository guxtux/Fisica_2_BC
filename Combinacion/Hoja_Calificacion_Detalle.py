# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
import csv
from numpy import array
import os

def calificacionCadena(final):
    calificacion2 =''
    
    if not(final == 'NP' or final == 'Monte Carlo' or final == 'Final'):
        
        calificacion1 = float(final)
    
        if 6 <= calificacion1 < 6.5:
            calificacion2 = '6 (Seis)'
        elif 6.6 <= calificacion1 < 7.5:
            calificacion2 = '7 (Siete)'
        elif 7.6 <= calificacion1 < 8.5:
            calificacion2 = '8 (Ocho)'
        elif 8.6 <= calificacion1 < 9.5:
            calificacion2 = '9 (Nueve)'
        else:
            calificacion2 = '10 (Diez)'

    return calificacion2

def concatenaNombre(nombres, apellido1, apellido2):
    return nombres + " " + apellido1 + " " + apellido2

def defineSaludo(entrada):
    if entrada == "1":
        return "Alumno"
    else:
        return "Alumna"

def elaboraConstancia(nombreCompleto, Presentacion, Personajes, Descripcion, Relacion, Bibliografia, Ortografia, Puntos, Comentarios):
    
    ruta = '2023_1_Cartas/'
    nombre_archivo = nombreCompleto.strip() + '_Evaluacion_Actividad_Personajes.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 7 de junio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = nombreCompleto + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la evaluación obtenida en tu actividad, en conformidad con la rúbrica que se anunció de manera oportuna.<br/><br/> Presentación: ' + Presentacion + '<br/> Personajes: ' + Personajes + '<br/> Personajes: ' + 'Descripción: ' + Descripcion + '<br/> Relación : ' + Relacion + '<br/> Bibliografía: ' + Bibliografia + '<br/> Ortografía: ' + Ortografia
    
    ptextomensaje = ptextomensaje + '<br><br> Puntos: ' + Puntos + 'Comentarios: ' + Comentarios
                        
    ptextomensaje = ptextomensaje + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def readinputdata(filename): 
    fichero=open(filename,'r') 
    f=[] 
    line='0' 
    with open(filename) as csv_file:
        for line in csv.reader(csv_file, delimiter=','): #
            if len(line)>0 : 
                f.append(line) 
    fichero.close() 
    return array(f)


data=readinputdata(r'Grupo_2023_1_Detalle.csv') 
# print (range(1, len(data))) #range(1,26)

for i in range(1, len(data)):
# for i in range(1, 2):
    nombreCompleto = concatenaNombre(data[i][2], data[i][0], data[i][1])
    numeroCuenta = data[i][3]
    promedioExamenes = data[i][4]
    aportaExamenes = data[i][5]
    entregaEjercicios = data[i][6]
    aportaEjercicios = data[i][7]
    promedio = data[i][8]
    ajuste = data[i][9]
    final = data[i][10]
    print(nombreCompleto, calificacionCadena(final))
    elaboraConstancia(nombreCompleto, numeroCuenta, promedioExamenes, \
                      aportaExamenes, entregaEjercicios, aportaEjercicios, \
                      promedio, ajuste, calificacionCadena(final))
