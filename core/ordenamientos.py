#Ordenar os paises (nombre, poblacion, superficie(ascendente o descendente)
#Ordenamiento borbuja - Por nombre
def ordenar_por_nombre(paises):
    cantidad_paises = len(paises)
    
    for i in range(cantidad_paises - 1):
        #Evita que sea comparados los paises ya ordenados
        for indice_actual in range(cantidad_paises - i - 1):
            nombre_actual = paises[indice_actual]["nombre"].lower()
            nombre_siguiente = paises[indice_actual + 1]["nombre"].lower()

            if nombre_actual > nombre_siguiente:
                paises[indice_actual], paises[indice_actual + 1] = paises[indice_actual + 1], paises[indice_actual]

    print("Países ordenados por nombre:\n")
    for p in paises:
        print(f"- {p['nombre']}; Superficie: {p['superficie']} km²; " f"Población: {p['poblacion']}; Continente: {p['continente']}")

    return paises

#Ordenamiento borbuja - Por poblacion
def ordenar_por_poblacion(paises):
    paises_validos = []
    
    for pais in paises:
        poblacion = pais.get("poblacion")
        #Garantizar que el valor sea numerico y valido
        if poblacion is None or not str(poblacion).isdigit():
            continue 
        #Hace una copia del diccionario original
        pais_copia = dict(pais)
        pais_copia["poblacion"] = int(poblacion)
        paises_validos.append(pais_copia)

    cantidad_paises = len(paises_validos)

    for i in range(cantidad_paises - 1):

        for indice_actual in range(cantidad_paises - i - 1):
            pop_actual = paises_validos[indice_actual]["poblacion"]
            pop_siguiente = paises_validos[indice_actual + 1]["poblacion"]

            if pop_actual > pop_siguiente:
                paises_validos[indice_actual], paises_validos[indice_actual + 1] = \
                    paises_validos[indice_actual + 1], paises_validos[indice_actual]

    print("Países ordenados por población (menor → mayor):")
    for pais in paises_validos:
        print(f"- {pais['nombre']}; Superficie: {pais['superficie']} km²; " f"Población: {pais['poblacion']}; Continente: {pais['continente']}")

    return paises_validos

#Ordenamiento borbuja - Por superficie

def ordenar_por_superficie(paises):
    paises_validos = []
    for pais in paises:
        superficie = pais.get("superficie")
        if superficie is None or not str(superficie).isdigit():
            continue
        #Hace una copia del diccionario original
        pais_copia = dict(pais)
        pais_copia["superficie"] = int(superficie)
        paises_validos.append(pais_copia)

    cantidad_paises = len(paises_validos)

    for i in range(cantidad_paises - 1):

        for indice_actual in range(cantidad_paises - i - 1):
            area_actual = paises_validos[indice_actual]["superficie"]
            area_siguiente = paises_validos[indice_actual + 1]["superficie"]

            if area_actual > area_siguiente:
                paises_validos[indice_actual], paises_validos[indice_actual + 1] = \
                    paises_validos[indice_actual + 1], paises_validos[indice_actual]

    print("Países ordenados por superficie (menor → mayor):\n")
    for pais in paises_validos:
        print(f"- {pais['nombre']}; Superficie: {pais['superficie']} km²; "f"Población: {pais['poblacion']}; Continente: {pais['continente']}")

    return paises_validos