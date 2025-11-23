"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        Columna_1 = [fila[0] for fila in reader]
    
    Register_letter= []
    
    def contador(letra):
        contador= 0
        for i in Columna_1:
            if i == letra:
                contador +=1
        return contador
    for j in Columna_1:
        contador(j)
        tupla= (j,contador(j))
        if tupla not in Register_letter:
            Register_letter.append(tupla)
    Register_letter.sort()
    return Register_letter
print(pregunta_02())