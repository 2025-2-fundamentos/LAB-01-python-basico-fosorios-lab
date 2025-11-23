"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
        Columna_1 = [fila[0] for fila in rows]
        Columna_2 = [fila[1] for fila in rows]
    Valores_letras= {}
    for i in range(len(Columna_2)):
        valor= int(Columna_2[i])
        letra= Columna_1[i]
        if valor not in Valores_letras:
            Valores_letras[valor]= [letra]
        else:
            Valores_letras[valor].append(letra)
    Resultado= []
    for j in Valores_letras:
        letras_unicas= list(set(Valores_letras[j]))
        letras_unicas.sort()
        tupla= (j,letras_unicas)
        Resultado.append(tupla)
    Resultado.sort()
    return Resultado
