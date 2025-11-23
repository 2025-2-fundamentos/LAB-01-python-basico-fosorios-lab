"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
        Columna_5 = [fila[4] for fila in rows]
    Diccionarios= []
    for i in Columna_5:
        Diccionarios.append(i.split(","))
    Claves_contador= {}
    for j in Diccionarios:
        for k in j:
            clave,valor= k.split(":")
            if clave not in Claves_contador:
                Claves_contador[clave]= 1
            else:
                Claves_contador[clave] += 1
    return Claves_contador
