"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
        Columna_1 = [fila[0] for fila in rows]
        Columna_2 = [fila[1] for fila in rows]
    Suma_letra= []
    def suma(letra):
        suma=0
        for i in range(len(Columna_1)):
            if Columna_1[i] == letra:
                suma += int(Columna_2 [i])
        return suma
    for j in Columna_1:
        suma(j)
        tupla= (j,suma(j))
        if tupla not in Suma_letra:
            Suma_letra.append(tupla)
    Suma_letra.sort()
    return Suma_letra
print(pregunta_03())
