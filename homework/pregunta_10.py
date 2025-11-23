"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
        Columna_1 = [fila[0] for fila in rows]
        Columna_4 = [fila[3] for fila in rows]
        Columna_5 = [fila[4] for fila in rows]
    Resultado= []
    for i in range(len(Columna_1)):
        letra= Columna_1[i]
        elementos_col4= Columna_4[i].split(",")
        elementos_col5= Columna_5[i].split(",")
        cantidad_col4= len(elementos_col4)
        cantidad_col5= len(elementos_col5)
        tupla= (letra,cantidad_col4,cantidad_col5)
        Resultado.append(tupla)
    return Resultado
