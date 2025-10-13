#Buscar un país por nombre (coincidencia parcial o exacta);
def buscar_por_nombre(paises, buscar, coincide=False): 
    paises_encontrados = []
    buscar = buscar.strip().lower()
    resultado = ''
    
    for pais in paises:
        nombre = pais.get("nombre").lower()
        if coincide: #Coincidencia exacta
            if nombre == buscar:
                paises_encontrados.append(pais)
        else: #Coincidencia parcial
            if buscar in nombre:
                paises_encontrados.append(pais)         
    if not paises_encontrados:
        resultado = f"No se encontraron países que coincidan con '{buscar}'."
    else:
        resultado = f"Se encontraron {len(paises_encontrados)} país(es) que coinciden con '{buscar}':\n"
        for p in paises_encontrados:
            resultado += f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}\n"
    return resultado

#Filtrar paises por continente;
def filtrar_por_continente(paises, continente):
    continente = continente.strip().lower()
    paises_filtrados = []
    resultado = ''
    
    for pais in paises:
        cont = pais.get("continente").lower()
        if continente in cont:
            paises_filtrados.append(pais)

    if not paises_filtrados:
        resultado = f"No se encontraron países en el continente '{continente}'."
    else:
        resultado = f"Se encontraron {len(paises_filtrados)} país(es) en el continente '{continente}':\n"
        for p in paises_filtrados:
            resultado += f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}\n"           
    return resultado

#Filtrar paises por poblacion;

def filtrar_por_poblacion(paises, min_pop, max_pop):
    min_pop = int(min_pop)
    max_pop = int(max_pop)
    paises_filtrados = []
    resultado = ''
    
    if max_pop < min_pop:
        min_pop, max_pop = max_pop, min_pop
    
    for pais in paises:
        poblacion = pais.get("poblacion")
        #Garantizar que el valor sea numerico y valido
        if poblacion is None or not str(poblacion).isdigit():
            continue
        poblacion = int(poblacion)

        if min_pop <= poblacion <= max_pop:
            paises_filtrados.append(pais)

    if not paises_filtrados:
        resultado = f"No se encontraron países con población entre {min_pop} y {max_pop}.\n"
    else:
        resultado = f"Se encontraron {len(paises_filtrados)} país(es) con población entre {min_pop} y {max_pop}:\n"
        for p in paises_filtrados:
            resultado += f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}\n"
    return resultado

#Filtrar paises por superficie;

def filtrar_por_superficie(paises, min_area, max_area):
    min_area = int(min_area)
    max_area = int(max_area)
    paises_filtrados = []
    resultado = ''
    
    if max_area < min_area:
        min_area, max_area = max_area, min_area
    
    for pais in paises:
        superficie = pais.get("superficie")
        #Garantizar que el valor sea numerico y valido
        if superficie is None or not str(superficie).isdigit():
            continue
        superficie = int(superficie)

        if min_area <= superficie <= max_area:
            paises_filtrados.append(pais)

    if not paises_filtrados:
        resultado = f"No se encontraron países con superficie entre {min_area} y {max_area}."
    else:
        resultado = f"Se encontraron {len(paises_filtrados)} país(es) con superficie entre {min_area} y {max_area}:\n"
        for p in paises_filtrados:
            resultado += f"- {p['nombre']}; Superficie: {p['superficie']} km²; Población: {p['poblacion']}; Continente: {p['continente']}\n"

    return resultado