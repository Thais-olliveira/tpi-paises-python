import csv
def cargar_paises(ruta: str) -> list[dict]:
    ruta = "data/paises_dataset.csv"

    paises = []

    with open(ruta, newline="", encoding="utf-8") as f:
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