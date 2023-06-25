#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:14:07 2022

@author: gustavo
"""

import pandas as pd
import hashlib
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors

def cargaArchivo(nombreArchivo):
    datos = pd.read_csv(nombreArchivo, sep = ',', header = 0)
    df = pd.DataFrame(datos)
    return df

def generaCadena(cuenta, nombre):
    cadena = cuenta + nombre
    hashed_string = hashlib.sha256(cadena.encode('utf-8')).hexdigest()
    return hashed_string

def quitaEspacios(cadenaEntrada):
    return cadenaEntrada.replace(" ", "")

def fechaActual(date):
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    dia = date.day
    mes = meses[date.month - 1]
    year = date.year
    cadena = 'Ciudad Universitaria a {0:} de {1:} de {2:}.'.format(dia, mes, year)
    return cadena

def elaboraConstancia(nombreCompleto, numeroCuenta, pTareas, pExamen, promedio, campana, calificacionFinal, comentarios, selloDigital, fecha):
    
    nombrePDF = nombreCompleto.strip() + ' Calificacion_Final_MAF' + '.pdf'
    pathArchivo = 'Cartas/'
    
    pathDocumento = os.path.join(pathArchivo, nombrePDF)
    
    objetoCanvas = Canvas(pathDocumento, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, fecha)
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = nombreCompleto + '. <br/> Número de cuenta: ' + numeroCuenta
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    cadenaCierre = '<br/><br/> Esta calificación se asentará en el acta oficial del curso, una vez que se haya realizado la captura y la firma electrónica, se les notificará vía correo electrónico, por lo que en un par de días ya podrán ver reflejada la calificación en su historial académico. <br/><br/>Atentamente, <br/>M. en C. Ramón Gustavo Contreras Mayén.'
    
    ptextomensaje = 'A continuación se presenta el resumen de la evaluación para el curso de Matemáticas  Avanzadas de la Física que cursaste durante el semestre 2022-2.  <br/><br/>' + \
'Promedio de tareas: ' + pTareas + '<br/> Promedio de exámenes: ' + pExamen + '<br/><br/>' + \
'De acuerdo al esquema de evaluación presentado al inicio del curso, con los promedios obtenidos de los ejercicios y los exámenes, tu promedio del curso es: ' + promedio  + '.<br/><br/>'

    if int(calificacionFinal) == 10:
        ptextomensaje = ptextomensaje + 'La calificación final que obtuviste es: ' + str(calificacionFinal) + '.<br/><br/>' + comentarios + cadenaCierre
    elif (6 <= int(calificacionFinal) < 10):
        ptextomensaje = ptextomensaje + 'Se aplicó un ajuste a la evaluación para todo el grupo, por lo que tu promedio queda en: ' + campana + ', de esta manera, la calificación final que obtuviste es: ' + str(calificacionFinal) + '.<br/><br/>' + comentarios + cadenaCierre
    elif int(calificacionFinal) == 5:
        ptextomensaje = ptextomensaje + 'La calificación final que obtuviste es: ' + str(calificacionFinal) + '.<br/><br/>' + comentarios + cadenaCierre
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    story3 = []
    
    cadenaHash256 = 'Sello digital: ' + selloDigital
    styles.add(ParagraphStyle(name='Sello', alignment=TA_LEFT, fontSize = 12, fontName='Courier', leading=12))
    story3.append(Paragraph(cadenaHash256, styles['Sello']))
    
    frame3 = Frame(50, 10, 6.5*inch, 1*inch, showBoundary=0)
    frame3.addFromList(story3, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def elaboraEvalRubrica(nombreCompleto, Presentacion, Personajes, Descripcion, Relacion, Bibliografia, Ortografia, Puntos, Comentarios):
    
    ruta = '2023_Evaluaciones/'
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
    
    ptextomensaje = 'A continuación se te presenta la evaluación obtenida en tu actividad de la revisión biográfica y de aportaciones de personajes en la física de fluidos, en conformidad con la rúbrica que se anunció de manera oportuna, se indica el puntaje obtenido y el total de puntos por la actividad.<br/><br/> Presentación: <u>' + Presentacion + '</u><br/> Personajes: <u>' + Personajes + '</u><br/> Descripción: <u>' + Descripcion + '</u><br/> Relación: <u>' + Relacion + '</u><br/> Bibliografía: <u>' + Bibliografia + '</u><br/> Ortografía: <u>' + Ortografia + '</u>'
    
    ptextomensaje = ptextomensaje + '<br/><br/>Puntos obtenidos:  <u>' + Puntos + '</u><br/><br/>Comentarios: ' + Comentarios
                        
    ptextomensaje = ptextomensaje + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def elaboraCartaPractica(Practica, Nombre, Preparacion, T_Experimental, Participacion, Reporte, Conclusiones, Calificacion, Comentarios):

    if Practica == "1":
        texto_Practica = "Práctica 1 - Propiedades de los Fluidos"
    else:
        texto_Practica = "Práctica 2 - Principio de Arquímedes"
    
    ruta = '2023_Evaluaciones/Practica_0' + Practica
    nombre_archivo = Nombre.strip() + '_Practica_0' + Practica + '.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 22 de junio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = Nombre + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 0.5*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la evaluación obtenida en tu reporte enviado de la ' + texto_Practica + ', en conformidad con la rúbrica que se anunció de manera oportuna, se indica el puntaje obtenido y el total de puntos por la actividad.<br/><br/>'

    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))

    # #Definimos otro frame.
    frame2 = Frame(50, 490, 6.5*inch, 1.2*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)

    story3 = []

    t = Table([ ['Preparación', 'Trab. Exp.', 'Participación', 'Reporte', 'Conclusiones'],
                [Preparacion, T_Experimental, Participacion, Reporte, Conclusiones]
                ],
                colWidths=75, rowHeights=20)
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTSIZE', (0, 0), (-1, 1), 12),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ('VALIGN', (1, 1), (-1, -1), 'MIDDLE')
                            ]))

    story3.append(t)

    #Definimos otro frame.
    frame3 = Frame(50, 430, 6.5*inch, 1*inch, showBoundary=0)
    frame3.addFromList(story3, objetoCanvas)

    story4 = []

    ptextomensaje2= '<br/><br/><b>Calificación:</b>  <u>' + Calificacion + '</u><br/><br/>Comentarios: ' + Comentarios
                        
    ptextomensaje2 = ptextomensaje2 + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'

    # styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story4.append(Paragraph(ptextomensaje2, styles['Justificado']))

    # #Definimos otro frame.
    frame4 = Frame(50, 150, 6.5*inch, 4.5*inch, showBoundary=0)
    frame4.addFromList(story4, objetoCanvas)

    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()