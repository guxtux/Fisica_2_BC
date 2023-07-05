# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:28:50 2023

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt

def vel(vi):
    vel= np.sqrt(2 * 9.91 * vi)
    return vel

def gasto(v):
    G = np.pi * 1 * v
    return G

def tiempo_caida(y):
    t = np.sqrt((2 * y) / 9.81)
    return t

def ejes1():
    plt.axis([0, 150, 0, 55])

h = 153
g = 9.81
v = []
gasto_salida = []
altura = []
valor_tiempo = []

a = range(13, 153, 20)
x = np.arange(0, 153)

for i in a:
    velocidad = vel(i)
    v.append(velocidad)
    gasto_salida.append(gasto(velocidad))
    altura.append(153 - i)

for i in altura:
    valor_tiempo.append(tiempo_caida(i))


# plt.figure(1)
# plt.plot(a, v, '+b')
# plt.axis([0, 150, 0, 55])
# plt.title('Valores de velocidad en los ductos de descarga')
# plt.savefig('Plot_Torricelli_01.eps', format='eps')
# ejes1()

# plt.figure(2)
# plt.plot(a, v, '+b')
# plt.plot(x, vel(x), ls='dashed', lw=0.7, color='r')
# plt.title('Valores de velocidad a lo largo de la cortina horizontal')
# plt.savefig('Plot_Torricelli_02.eps', format='eps')
# ejes1()

# plt.figure(3)
# plt.plot(a, gasto_salida, 'or')
# plt.title('Gasto de salida contra velocidad $m^3/s$')
# plt.savefig('Plot_Torricelli_03.eps', format='eps')
# plt.axis([0, 140, 0, 170])

plt.figure(4)
plt.plot(a, valor_tiempo)



plt.show()
