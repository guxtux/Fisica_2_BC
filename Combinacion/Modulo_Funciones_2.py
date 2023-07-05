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
from reportlab.platypus import Paragraph, Frame, Table, TableStyle, PageBreak
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

def elaboraCartaPractica(Nombre, Preparacion, Trabajo_E, Participacion, Reporte, Conclusiones, Calificacion, Comentarios):
    
    ruta = 'Laboratorio/Practica_02'
    nombre_archivo = Nombre.strip() + '_Practica_02.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 22 de junio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = Nombre + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la evaluación obtenida en tu reporte de la Práctica 2 - Errores de Medición en Física, en conformidad con la rúbrica que se anunció de manera oportuna, se indica el puntaje obtenido y el total de puntos por la actividad.<br/><br/> Preparación: <u>' + Preparacion + '</u><br/> Trabajo Experimental: <u>' + Trabajo_E + '</u><br/> Participación: <u>' + Participacion + '</u><br/> Reporte: <u>' + Reporte + '</u><br/> Conclusiones: <u>' + Conclusiones + '</u>'
    
    ptextomensaje = ptextomensaje + '<br/><br/>Calificación:  <u>' + Calificacion + '</u><br/><br/>Comentarios: ' + Comentarios
                        
    ptextomensaje = ptextomensaje + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def elaboraCartaConcentrado(Estudiante, Webinar, Personajes, Densidades, Conversion, M_Amb, Ejer_Pascal, Puntos, Eval_Continua, Practica_1, Practica_2, Laboratorio):

    ruta = 'Evaluacion_Continua/Parcial_01'
    nombre_archivo = Estudiante.strip() + '_Concentrado_Parcial_01.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 20 de junio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = Estudiante + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 650, 6.5*inch, 0.5*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la relación de actividades de Evaluación Continua, así como de los reportes de las Prácticas de Laboratorio, que forman parte de la evaluación del Primer Examen Parcial del curso de Física 2.<br/><br/><b>Evaluación Continua.</b><br/> Las actividades de evaluación continua, el puntaje a obtener en la actividad, así como las fechas de asignación y entrega por Teams son las siguientes:'
    
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))

    #Definimos otro frame.
    frame2 = Frame(50, 510, 6.5*inch, 2*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)

    story3 = []

    colWidths=(1.6*inch, 0.6*inch, 1.5*inch, 1.25*inch,)

    t1 = Table([ ['Actividad', 'Puntos', 'Fecha asignación', 'Fecha entrega'],
                ['Webinar', '1', '17 de mayo', '17 de mayo'],
                ['Personajes Fluidos', '3', '21 de mayo', '28 de mayo'],
                ['Densidades', '1', '23 de mayo', '28 de mayo'],
                ['Unidades Presión', '1', '29 de mayo', '4 de junio'],
                ['Medio Ambiente', '1', '7 de junio', '7 de junio'],
                ['Ejercicios Pascal', '2', '7 de junio', '11 de junio']
                ],
                colWidths, rowHeights=25)
    t1.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTSIZE', (0, 0), (-1, -1), 12),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
                            ]))
    
    story3.append(t1)

    #Definimos otro frame.
    frame3 = Frame(50, 320, 6.5*inch, 2.75*inch, showBoundary=0)
    frame3.addFromList(story3, objetoCanvas)

    story4 = []
    
    ptextomensaje = 'El total de puntos a obtener en las actividades es de 9. La suma de tu puntaje se divide entre 9. <br/><br/>Lo que enviaste:<br/>'

    story4.append(Paragraph(ptextomensaje, styles['Justificado']))

    columnas1 = (0.8*inch, 1*inch, 0.6*inch, 1*inch, 1*inch, 1*inch, 0.8*inch)
    t2 = Table([ ['Webinar', 'Personajes', 'Dens.', 'U. Presión', 'Medio Amb.', 'Ejer. Pascal', 'Puntos'],
                [Webinar, Personajes, Densidades, Conversion, M_Amb, Ejer_Pascal, Puntos]
                ],
                columnas1, rowHeights=20)

    t2.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTSIZE', (0, 0), (-1, 1), 12),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ('VALIGN', (1, 1), (-1, -1), 'MIDDLE')
                            ])) 

    story4.append(t2)

    textopuntaje = '<br/><b>Calificación de Evaluación Continua: ' + Eval_Continua +'</b>'

    story4.append(Paragraph(textopuntaje, styles['Justificado']))
    # story4.append(PageBreak())

    # Definimos otro frame.
    frame3 = Frame(50, 160, 6.5*inch, 2.3*inch, showBoundary=0)
    frame3.addFromList(story4, objetoCanvas)

    objetoCanvas.showPage()

    story5 = []
    
    ptextolaboratorio = '<b>Laboratorio.</b><br/>Se consideran las dos prácticas realizadas, se presenta el puntaje a obtener en la práctica, así como las fechas de asignación y entrega por grupo:<br/><br/>'
    
    story5.append(Paragraph(ptextolaboratorio, styles['Justificado']))

    colWidths=(0.6*inch, 1*inch, 0.6*inch, 1.45*inch, 1.25*inch,)

    t3 = Table([ ['Grupo', 'Práctica', 'Puntos', 'Fecha asignación', 'Fecha entrega'],
                 ['41B', 'Práctica 1', '10', '25 de mayo', '31 de mayo'],
                 ['41C', 'Práctica 1', '10', '26 de mayo', '1 de junio'],
                 ['41B', 'Práctica 2', '10', '1 de junio', '7 de junio'],
                 ['41C', 'Práctica 2', '10', '2 de junio', '8 de junio']
                 ],
                 colWidths, rowHeights=25)
    t3.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTSIZE', (0, 0), (-1, -1), 12),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
                            ]))
    
    story5.append(t3)

    # #Definimos otro frame.
    frame4 = Frame(50, 500, 6.5*inch, 3.1*inch, showBoundary=0)
    frame4.addFromList(story5, objetoCanvas)

    story6 = []
    
    ptextomensaje2 = 'En tu registro se tiene lo siguiente:<br/>'

    story6.append(Paragraph(ptextomensaje2, styles['Justificado']))

    t4 = Table([ ['Práctica 1', 'Práctica 2', 'Promedio'],
                [Practica_1, Practica_2, Laboratorio]
                ],
                colWidths=70, rowHeights=20)

    t4.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTSIZE', (0, 0), (-1, 1), 12),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ('VALIGN', (1, 1), (-1, -1), 'MIDDLE')
                            ])) 

    story6.append(t4)

    textopuntaje2 = '<br/><b>Calificación de Laboratorio: ' + Laboratorio +'</b>'

    story6.append(Paragraph(textopuntaje2, styles['Justificado']))

    #Definimos otro frame.
    frame5 = Frame(50, 400, 6.5*inch, 1.5*inch, showBoundary=0)
    frame5.addFromList(story6, objetoCanvas)

    story7 = []

    ptextocalificaciones = "<br/></b</>La calificación del PRIMER EXAMEN PARCIAL se obtiene, primero al multiplicar cada elemento por el correspondiente peso, luego se suman los puntajes, el resultado es tu calificación del primer examen parcial, solo queda pendiente anotar tu calificación del examen.<br/><br/>"

    story7.append(Paragraph(ptextocalificaciones, styles['Justificado']))

    columnas = (1.75*inch, 1.2*inch, 1*inch, 1*inch)
    t5 = Table([['Elemento', 'Calificación', 'Peso', 'Puntaje'],
                ['Evaluación continua', Eval_Continua, "35%", float(Eval_Continua)*0.5],
                ['Examen', '', '35%', ''],
                ['Laboratorio', Laboratorio, '30%', round(float(Laboratorio)*0.3, 2)]                
                ],
                columnas, rowHeights=25)
    t5.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTSIZE', (0, 0), (-1, -1), 12),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
                            ]))
    
    story7.append(t5)

    ptextomensajefinal= '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.<br/>Profesor del curso de Física 2.'

    
    story7.append(Paragraph(ptextomensajefinal, styles['Justificado']))

    #Definimos otro frame.
    frame6 = Frame(50, 100, 6.5*inch, 4.35*inch, showBoundary=0)
    frame6.addFromList(story7, objetoCanvas)

    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()
    
#---------------------------

def elaboraCartaConcentradoSemanal(Semana, Estudiante, Webinar, Faltas_Teo, Faltas_Lab, Previo_Lab):

    ruta = 'Evaluacion_Continua/Parcial_02'
    nombre_archivo = Estudiante.strip() + '_Concentrado_Semana_0' + Semana + '.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 2 de julio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = Estudiante + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 650, 6.5*inch, 0.5*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la relación de asistentes, actividades de Evaluación Continua, y del trabajo de Laboratorio, para la semana ' + Semana  + '.'
    
    if Semana == '7':
        fecha_semana = '<br/><br/>Del 26 al 30 de junio de 2023.'
    
    ptextomensaje = ptextomensaje + fecha_semana
    
        
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))

    #Definimos otro frame.
    frame2 = Frame(50, 510, 6.5*inch, 2*inch, showBoundary=1)
    frame2.addFromList(story2, objetoCanvas)

    # story3 = []

    # colWidths=(1.6*inch, 0.6*inch, 1.5*inch, 1.25*inch,)

    # t1 = Table([ ['Actividad', 'Puntos', 'Fecha asignación', 'Fecha entrega'],
    #             ['Webinar', '1', '17 de mayo', '17 de mayo'],
    #             ['Personajes Fluidos', '3', '21 de mayo', '28 de mayo'],
    #             ['Densidades', '1', '23 de mayo', '28 de mayo'],
    #             ['Unidades Presión', '1', '29 de mayo', '4 de junio'],
    #             ['Medio Ambiente', '1', '7 de junio', '7 de junio'],
    #             ['Ejercicios Pascal', '2', '7 de junio', '11 de junio']
    #             ],
    #             colWidths, rowHeights=25)
    # t1.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #                         ('FONTSIZE', (0, 0), (-1, -1), 12),
    #                         ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #                         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    #                         ]))
    
    # story3.append(t1)

    # #Definimos otro frame.
    # frame3 = Frame(50, 320, 6.5*inch, 2.75*inch, showBoundary=0)
    # frame3.addFromList(story3, objetoCanvas)

    # story4 = []
    
    # ptextomensaje = 'El total de puntos a obtener en las actividades es de 9. La suma de tu puntaje se divide entre 9. <br/><br/>Lo que enviaste:<br/>'

    # story4.append(Paragraph(ptextomensaje, styles['Justificado']))

    # columnas1 = (0.8*inch, 1*inch, 0.6*inch, 1*inch, 1*inch, 1*inch, 0.8*inch)
    # t2 = Table([ ['Webinar', 'Personajes', 'Dens.', 'U. Presión', 'Medio Amb.', 'Ejer. Pascal', 'Puntos'],
    #             [Webinar, Personajes, Densidades, Conversion, M_Amb, Ejer_Pascal, Puntos]
    #             ],
    #             columnas1, rowHeights=20)

    # t2.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #                         ('FONTSIZE', (0, 0), (-1, 1), 12),
    #                         ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #                         ('VALIGN', (1, 1), (-1, -1), 'MIDDLE')
    #                         ])) 

    # story4.append(t2)

    # textopuntaje = '<br/><b>Calificación de Evaluación Continua: ' + Eval_Continua +'</b>'

    # story4.append(Paragraph(textopuntaje, styles['Justificado']))
    # # story4.append(PageBreak())

    # # Definimos otro frame.
    # frame3 = Frame(50, 160, 6.5*inch, 2.3*inch, showBoundary=0)
    # frame3.addFromList(story4, objetoCanvas)

    # objetoCanvas.showPage()

    # story5 = []
    
    # ptextolaboratorio = '<b>Laboratorio.</b><br/>Se consideran las dos prácticas realizadas, se presenta el puntaje a obtener en la práctica, así como las fechas de asignación y entrega por grupo:<br/><br/>'
    
    # story5.append(Paragraph(ptextolaboratorio, styles['Justificado']))

    # colWidths=(0.6*inch, 1*inch, 0.6*inch, 1.45*inch, 1.25*inch,)

    # t3 = Table([ ['Grupo', 'Práctica', 'Puntos', 'Fecha asignación', 'Fecha entrega'],
    #              ['41B', 'Práctica 1', '10', '25 de mayo', '31 de mayo'],
    #              ['41C', 'Práctica 1', '10', '26 de mayo', '1 de junio'],
    #              ['41B', 'Práctica 2', '10', '1 de junio', '7 de junio'],
    #              ['41C', 'Práctica 2', '10', '2 de junio', '8 de junio']
    #              ],
    #              colWidths, rowHeights=25)
    # t3.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #                         ('FONTSIZE', (0, 0), (-1, -1), 12),
    #                         ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #                         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    #                         ]))
    
    # story5.append(t3)

    # # #Definimos otro frame.
    # frame4 = Frame(50, 500, 6.5*inch, 3.1*inch, showBoundary=0)
    # frame4.addFromList(story5, objetoCanvas)

    # story6 = []
    
    # ptextomensaje2 = 'En tu registro se tiene lo siguiente:<br/>'

    # story6.append(Paragraph(ptextomensaje2, styles['Justificado']))

    # t4 = Table([ ['Práctica 1', 'Práctica 2', 'Promedio'],
    #             [Practica_1, Practica_2, Laboratorio]
    #             ],
    #             colWidths=70, rowHeights=20)

    # t4.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #                         ('FONTSIZE', (0, 0), (-1, 1), 12),
    #                         ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #                         ('VALIGN', (1, 1), (-1, -1), 'MIDDLE')
    #                         ])) 

    # story6.append(t4)

    # textopuntaje2 = '<br/><b>Calificación de Laboratorio: ' + Laboratorio +'</b>'

    # story6.append(Paragraph(textopuntaje2, styles['Justificado']))

    # #Definimos otro frame.
    # frame5 = Frame(50, 400, 6.5*inch, 1.5*inch, showBoundary=0)
    # frame5.addFromList(story6, objetoCanvas)

    # story7 = []

    # ptextocalificaciones = "<br/></b</>La calificación del PRIMER EXAMEN PARCIAL se obtiene, primero al multiplicar cada elemento por el correspondiente peso, luego se suman los puntajes, el resultado es tu calificación del primer examen parcial, solo queda pendiente anotar tu calificación del examen.<br/><br/>"

    # story7.append(Paragraph(ptextocalificaciones, styles['Justificado']))

    # columnas = (1.75*inch, 1.2*inch, 1*inch, 1*inch)
    # t5 = Table([['Elemento', 'Calificación', 'Peso', 'Puntaje'],
    #             ['Evaluación continua', Eval_Continua, "35%", float(Eval_Continua)*0.5],
    #             ['Examen', '', '35%', ''],
    #             ['Laboratorio', Laboratorio, '30%', round(float(Laboratorio)*0.3, 2)]                
    #             ],
    #             columnas, rowHeights=25)
    # t5.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #                         ('FONTSIZE', (0, 0), (-1, -1), 12),
    #                         ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #                         ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    #                         ]))
    
    # story7.append(t5)

    # ptextomensajefinal= '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.<br/>Profesor del curso de Física 2.'

    
    # story7.append(Paragraph(ptextomensajefinal, styles['Justificado']))

    # #Definimos otro frame.
    # frame6 = Frame(50, 100, 6.5*inch, 4.35*inch, showBoundary=0)
    # frame6.addFromList(story7, objetoCanvas)

    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()