"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
        Columna_1 = [fila[0] for fila in rows]
        Columna_2 = [fila[1] for fila in rows]
    Resultado= []
    def max_min(letra):
        valores= []
        for i in range(len(Columna_1)):
            if Columna_1[i] == letra:
                valores.append(int(Columna_2[i]))
        maximo= max(valores)
        minimo= min(valores)
        return (maximo,minimo)
    for j in Columna_1:
        tupla= (j, max_min(j)[0], max_min(j)[1])
        if tupla not in Resultado:
            Resultado.append(tupla)
    Resultado.sort()
    return Resultado   