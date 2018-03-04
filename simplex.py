from fractions import Fraction

total_columnas = int(input("Cuantas departamentos se tienen: "))
columnas = total_columnas
total_columnas = ((total_columnas + 1) * 2) + 1
filas = columnas + 1

# Creando una lista con una lista
w, h = total_columnas, filas;
Matrix = [[0 for x in range(w)] for y in range(h)]

gananciadepto = []

# Llenado de valores  de deptos
for i in range(0, columnas):
    gananciadepto.append(Fraction(input(f"Introduce cual es el valor del depto {i + 1}: ")))

# Llenado de datos
print("Ordena los datos de la tabla (solo los numeros): ")
for i in range(0, filas):
    print("---------------------------------------------")
    for j in range(0, total_columnas):
        Matrix[i][j] = Fraction(input(f"Valor de la fila: {i + 1} columna: {j + 1} -> "))

# Imprimiendo la tabla introducida
for i in Matrix:
    print(i)

# Haciendo las tablas
contador = filas - 1
columna_optima = columnas
value_depto_select = 0
zuno = 0
valor_de_columna_optima = 2

while contador > 0:

    # Mostrando las diviciones de la columna optima
    if columna_optima > 0:
        for i in range(0, filas):
            if Matrix[i][1] == 0 or Matrix[i][valor_de_columna_optima] == 0:
                print(f"El renglon {i+1} Contiene una divicion entre 0 por lo tanto no es una eleccion")
            else:
                print(f"Renglon: {i+1}, {Matrix[i][1]} / {Matrix[i][valor_de_columna_optima]} = {Fraction(Matrix[i][1] / Matrix[i][valor_de_columna_optima])}")
        columna_optima -= 1
        valor_de_columna_optima += 1

    fila_utilizada = int(input("Ingrese cual es la fila del valor que va a utilizar: "))
    fila_utilizada -= 1
    eleccion_menor = Fraction(input("Ingrese el valor a utilizar: "))

    # Modificando la tabla
    Matrix[fila_utilizada][0] = gananciadepto[value_depto_select]
    for i in range(1, total_columnas):
        if Matrix[fila_utilizada][i] != 0:
            Matrix[fila_utilizada][i] /= eleccion_menor

    # Remplazando todas las filas
    for i in range(0, filas):
        if i != fila_utilizada:

            if Matrix[i][valor_de_columna_optima - 1] != 0:
                eleccion_menor = Matrix[i][valor_de_columna_optima - 1]
            else:
                eleccion_menor = 0

            for j in range(1, total_columnas):
                Matrix[i][j] = Matrix[i][j] + (-1 * (eleccion_menor * Matrix[fila_utilizada][j]))

    # Conociendo el valor de Z1
    for i in range(0, filas):
        if Matrix[i][0] != 0:
            temp = Matrix[i][0] * Matrix[i][1]
            zuno += temp

    # imprimiendo la Matriz y el valor de Z1
    for i in Matrix:
        print(i)
    
    print(f"Valor de Z1 = {zuno}")

    value_depto_select += 1
    contador -= 1
    zuno = 0
"""
By: Alfonso Candiani Jaramillo

                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
  jgs \""--..__                              __..--""/
       '._     https://candianijaramillo.com"""
