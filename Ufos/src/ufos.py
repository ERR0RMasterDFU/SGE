import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple, Counter, defaultdict


def lee_avistamientos(fichero):
    res=[]
    with open (fichero, encoding = 'uft-8') as f:
        lector = 

        for x in lector:
            fecha_hora = datatime.striptime(fecha_hora)
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistamiento(fecha_hora, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res = append(tupla)