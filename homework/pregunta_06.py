"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
    Claves_valores= {}
    for j in Diccionarios:
        for k in j:
            clave,valor= k.split(":")
            if clave not in Claves_valores:
                Claves_valores[clave]= [int(valor)]
            else:
                Claves_valores[clave].append(int(valor))
    Resultado= []
    for l in Claves_valores:
        minimo= min(Claves_valores[l])
        maximo= max(Claves_valores[l])
        tupla= (l,minimo,maximo)
        Resultado.append(tupla)
    Resultado.sort()
    return Resultado
