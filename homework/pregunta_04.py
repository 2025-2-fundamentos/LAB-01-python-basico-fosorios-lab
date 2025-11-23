"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    import csv
    ruta="files/input/data.csv"
    with open(ruta, newline="",encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        rows = list(reader)
        Columna_3 = [fila[2] for fila in rows]
    Columna_separada= []
    for i in Columna_3:
        fecha= i.split("-")
        Columna_separada.append(fecha)
    Meses= []
    for j in Columna_separada:
        Meses.append(j[1])
    def contador_mes(mes):
        contador=0
        for k in Meses:
            if k == mes:
                contador += 1
        return contador
    Resultado= []
    for l in Meses:
        contador_mes(l)
        tupla= (l,contador_mes(l))
        if tupla not in Resultado:
            Resultado.append(tupla) 
    Resultado.sort()

    return Resultado
print(pregunta_04())