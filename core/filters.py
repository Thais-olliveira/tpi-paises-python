#Buscar un país por nombre (coincidencia parcial o exacta);
def buscar_por_nombre(paises, buscar, coincide=False): 
    resultado = []
    buscar = buscar.strip().lower()
    
    for pais in paises:
        nombre = pais.get("nombre").lower()
        if coincide: #Coincidencia exacta
            if nombre == buscar:
                resultado.append(pais)
        else: #Coincidencia parcial
            if buscar in nombre:
                resultado.append(pais)         
    if not resultado:
        print(f"No se encontraron países que coincidan con '{buscar}'.")
    else:
        print(f"Se encontraron {len(resultado)} país(es) que coinciden con '{buscar}':")
        for p in resultado:
            print(f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}")

    return resultado

#Filtrar paises por continente;
def filtrar_por_continente(paises, continente):
    continente = continente.strip().lower()
    resultado = []
    
    for pais in paises:
        cont = pais.get("continente").lower()
        if cont == continente:
            resultado.append(pais)

    if not resultado:
        print(f"No se encontraron países en el continente '{continente}'.")
    else:
        print(f"Se encontraron {len(resultado)} país(es) en el continente '{continente}':")
        for p in resultado:
            print(f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}")
    
    return resultado

#Filtrar paises por poblacion;

def filtrar_por_poblacion(paises, min_pop=0, max_pop=-1):
    resultado = []
    for pais in paises:
        poblacion = pais.get("poblacion")
        #Garantizar que el valor sea numerico y valido
        if poblacion is None or not str(poblacion).isdigit():
            continue
        poblacion = int(poblacion)

        if (poblacion >= min_pop) and (max_pop == -1 or poblacion <= max_pop):
            resultado.append(pais)

    if not resultado:
        print(f"No se encontraron países con población entre {min_pop} y {max_pop}.")
    else:
        print(f"Se encontraron {len(resultado)} país(es) con población entre {min_pop} y {max_pop}:")
        for p in resultado:
            print(f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}")

    return resultado

#Filtrar paises por superficie;

def filtrar_por_superficie(paises, min_area=0, max_area=-1):
    resultado = []
    for pais in paises:
        superficie = pais.get("superficie")
        #Garantizar que el valor sea numerico y valido
        if superficie is None or not str(superficie).isdigit():
            continue
        superficie = int(superficie)

        if (superficie >= min_area) and (max_area == -1 or superficie <= max_area):
            resultado.append(pais)

    if not resultado:
        print(f"No se encontraron países con superficie entre {min_area} y {max_area}.")
    else:
        print(f"Se encontraron {len(resultado)} país(es) con superficie entre {min_area} y {max_area}:")
        for p in resultado:
            print(f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}")

    return resultado