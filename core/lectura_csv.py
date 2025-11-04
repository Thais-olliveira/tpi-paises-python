import csv
import os

def cargar_paises():
    ruta_csv = "data/paises_dataset.csv"
    paises = []

    if not os.path.exists(ruta_csv):
        print("El archivo CSV no existe")
        return paises

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        columnas = next(lector)
        columnas = [i.lower().strip() for i in columnas]

        # Lecturas de las lineas
        for i, fila in enumerate(lector, start=2):
            nombre, superficie, poblacion, continente = [x.strip() for x in fila]

            paises.append({
                "nombre": nombre,
                "superficie": int(superficie),
                "poblacion": int(poblacion),
                "continente": continente
            })

    return paises