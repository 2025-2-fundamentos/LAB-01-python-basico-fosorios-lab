"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv

    ruta = "files/input/data.csv"  # ruta relativa al repo
    suma = 0.0
    count = 0
    errores = []

    with open(ruta, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')  # el archivo es TSV (tab-separated)
        for i, row in enumerate(reader, start=1):
            # Ignorar filas que no tengan al menos 2 columnas
            if len(row) < 2:
                errores.append((i, "menos de 2 columnas"))
                continue

            val = row[1].strip()
            if val == "":
                errores.append((i, "vacío"))
                continue

            # Normalizaciones comunes: coma decimal -> punto
            val_norm = val.replace(",", ".")
            try:
                num = float(val_norm)   # usar float para aceptar enteros y decimales
                suma += num
                count += 1
            except ValueError:
                errores.append((i, val))

    # Mostrar resultado: si todos fueron enteros, mostrar como int
    if suma.is_integer():
        suma_mostrar = int(suma)
    else:
        suma_mostrar = suma

    return suma_mostrar
print(pregunta_01())

