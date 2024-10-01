# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 1

# Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura:
# El área de un rectángulo se obtiene al multiplicar la base por la altura.

base = input('Por favor, dime la longitud de la base (m).')
altura = input('Por favor, dime la longitud de la altura (m).')

def area_rectangulo(base, altura):
    area = float(base)*float(altura)
    print('El área del rectángulo es de {} m2.'.format(area))

area_rectangulo(base, altura)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

