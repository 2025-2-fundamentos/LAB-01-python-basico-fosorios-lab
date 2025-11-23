"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
        Columna_2 = [fila[1] for fila in rows]
        Columna_4 = [fila[3] for fila in rows]
    Letras_suma= {}
    for i in range(len(Columna_4)):
        letras= Columna_4[i].split(",")
        valor= int(Columna_2[i])
        for j in letras:
            if j not in Letras_suma:
                Letras_suma[j]= valor
            else:
                Letras_suma[j] += valor
    return dict(sorted(Letras_suma.items()))
