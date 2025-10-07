import csv
#Lee el archivo CSV y genera una lista de diccionarios con los países.
def cargar_paises(ruta: str) -> list[dict]:

    paises = []

    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        columnas = next(lector) 
        columnas = [i.lower().strip() for i in columnas]
        
        # Lecturas de las lineas
        for i, fila in enumerate(lector, start=2):
            #Manejo de errores(try-except)
            try:
                nombre, superficie, poblacion, continente = [x.strip() for x in fila]

                paises.append({
                    "Nombre": nombre,
                    "Superficie": int(superficie),
                    "Población": int(poblacion),
                    "Continente": continente
                })
            except Exception:
                print(f"Línea {i}: error en el formato de datos")
    return paises
