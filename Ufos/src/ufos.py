import csv
from datetime import datetime
from math import sqrt
from collections import namedtuple

#Creación de una tupla coon nombre
Avistamiento = namedtuple('Avistamiento', 'fechaHora, ciudad, estado, forma, duracion, comentarios, latitud, longitud')

#Funcion de lectura que crea una lista de avistamientos
def lee_avistamientos(fichero):
    
    res=[]
    f = open(fichero) 
    with open(fichero, encoding='utf-8') as f: #ABRE EL FICHERO Y LO LLAMO F ES LO MISMO QUE:  f = open (fichero, encoding = 'uft-8')
        lector = csv.reader(f) #Lee el fichero f
        next(lector)

        for x in lector: #HAY QUE CASTEAR LOS ATRIBUTOS PORQUE SE DETECTAN COMO STRINGS
            fecha_hora = x[0]
            fecha_hora_cast = datetime.strptime(fecha_hora, '%m/%d/%Y %H:%M')
            ciudad = x[1]
            estado = x[2]
            forma = x[3]
            duracion = int(x[4])
            comentarios = x[5]
            latitud = float(x[6])
            longitud = float(x[7])
            tupla = Avistamiento(fecha_hora_cast, ciudad, estado, forma, duracion, comentarios, latitud, longitud)
            res.append(tupla)

        return res


def duracion_total(registro, estado):
    duracion = sum(avistamiento.duracion for avistamiento in registro if estado.lower() == avistamiento.estado.lower())
    return duracion;


def comentario_mas_largo(registros, anyo, palabra):

    elegido = ""
    avistamientoElegido = None
    fallo = "No se ha encontrado"

    for avistamiento in registros:
        if anyo == avistamiento.fechaHora.strftime('%Y') and palabra in avistamiento.comentarios:
            if len(elegido) < len(avistamiento.comentarios):
                elegido = avistamiento.comentarios
                avistamientoElegido = avistamiento

    return avistamientoElegido if avistamientoElegido else fallo

