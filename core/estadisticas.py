#Calculos estadisticos (Pais com maior y menor poblacion; promedio de poblacion, promedio de superficie
# cantidad de paises por continente)

#País con mayor y menor población
def mayor_menor_poblacion (paises):
    paises_validos = []
    
    for pais in paises:
        poblacion = pais.get("poblacion")
        #Garante que el valor sea numerico y valido
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

    menor = paises_validos[0]
    mayor = paises_validos[-1]
    
    print("País con menor población:", menor["nombre"], "-", menor["poblacion"])
    print("País con mayor población:", mayor["nombre"], "-", mayor["poblacion"])
    
#Promedio de poblacion
def promedio_poblacion(paises):
    poblaciones = []

    for pais in paises:
        poblacion = pais.get("poblacion")
        if poblacion is None or not str(poblacion).isdigit():
            continue
        poblaciones.append(int(poblacion))

    if not poblaciones:
        return 0

    promedio = sum(poblaciones) / len(poblaciones)
    return promedio

#Promedio de superficie
def promedio_superficie(paises):
    superficies = []

    for pais in paises:
        superficie = pais.get("superficie")
        if superficie is None or not str(superficie).isdigit():
            continue
        superficies.append(int(superficie))

    if not superficies:
        return 0

    promedio = sum(superficies) / len(superficies)
    return promedio

#Cantidad paises por continente
def cantidad_paises_continente(paises):
    contador = {}

    for pais in paises:
        continente = pais.get("continente", "").strip()
        if not continente:
            continue

        # Incrementa el contador del continente
        if continente in contador:
            contador[continente] += 1
        else:
            contador[continente] = 1

    print("\nCantidad de países por continente:")
    for continente, cantidad in contador.items():
        print(f"- {continente}: {cantidad} país(es)")

    return contador