import csv

def validar_nombre(nombre):
    """
    Validación que el nombre ingresado no sea vacio
    """
    if not nombre.strip():
        print("El nombre del pais no puede estar vacío. Intenta nuevamente.")
        return None
    return nombre.strip()

def validar_superficie(superficie):
    """
    Validación que la superficie no sea vacia y sea un numero entero positivo
    """
    if not superficie.strip():
        print("La superficie no puede estar vacía")
        return None
    if not superficie.isdigit() or int(superficie) <= 0:
        print("La superficie debe ser un número entero positivo")
        return None
    return int(superficie)

def validar_poblacion(poblacion):
    """
    Validación que la poblacion no sea vacia y sea un numero entero positivo
    """
    if not poblacion.strip():
        print("La población no puede estar vacía")
        return None
    if not poblacion.isdigit() or int(poblacion) <= 0:
        print("La población debe ser un número entero positivo")
        return None
    return int(poblacion)

def validar_continente(continente):
    """
    Validación que el continente ingresado no sea vacio
    """
    if not continente.strip():
        print("El continente no puede estar vacío")
        return None
    return continente.strip()

def obtener_nombres_paises(ruta_csv: str):
    """
    Lee el archivo CSV y devulve una lista con los nombres de los paises
    """
    paises_existentes = []
    with open(ruta_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises_existentes.append(fila["nombre"].strip().lower())
    return paises_existentes

def leer_paises_completos(ruta_csv: str):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios completo (nombre,superficie, 
    poblacion y continente)
    """
    paises = []
    with open(ruta_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append(fila)
    return paises

def guardar_pais_nuevo(ruta_csv: str, nombre: str, superficie: int, poblacion: int, continente: str):
    """
    Agrega un nuevo pais
    """
    with open(ruta_csv, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, superficie, poblacion, continente])
        
def reescribir_archivo(ruta_csv: str, paises: list):
    """
    Reescribe el archivo CSV cuando se realiza actualizaciones en los registros
    """
    campos = ["nombre", "superficie", "poblacion", "continente"]
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)
        
        
def elegir_continente_desde_lista():
    Continentes_disponibles = [
    "África",
    "América del Norte",
    "América del Sur",
    "Asia",
    "Europa",
    "Oceanía",
    "Antártida",
]
    while True:
        print("\n--- Selección de continente ---")
        for i, cont in enumerate(Continentes_disponibles, start=1):
            print(f"{i}. {cont}")
        print("0. Cancelar")

        opcion = input("Elija una opción: ").strip()

        if opcion == "0":
            print("Operación cancelada.")
            return None

        if opcion.isdigit():
            indice = int(opcion)
            if 1 <= indice <= len(Continentes_disponibles):
                continente = Continentes_disponibles[indice - 1]
                print(f"Has elegido: {continente}")
                return continente

        print("Opción inválida. Intente nuevamente.")

#Agregar un nuevo país

def agregar_pais(ruta_csv: str):
    print("\n---- Agregar un nuevo país ------")
    print("Por favor ingrese los datos del pais que desea agregar")
    
    nombre = validar_nombre(input("Nombre del país: "))
    if nombre is None:
        return
    
    paises_existentes = obtener_nombres_paises(ruta_csv)
    if nombre.lower() in paises_existentes:
        print(f"No fue posible agregar. El país '{nombre}' ya existe en el CSV")
        return
    
    superficie = validar_superficie(input("Superficie (km²): "))
    if superficie is None:
        return
    
    poblacion = validar_poblacion(input("Población: "))
    if poblacion is None:
        return
    
    continente = elegir_continente_desde_lista()
    if continente is None:
        return

    guardar_pais_nuevo(ruta_csv, nombre, superficie, poblacion, continente)
    print(f"País agregado correctamente: {nombre}")

#Actualizar populacion y superficie;

def actualizar_pais(ruta_csv: str):
    print("\n---- Actualizar país ----")
    nombre = validar_nombre(input("Nombre del país que desea actualizar: ").strip().lower())
    if nombre is None:
        return

    paises = leer_paises_completos(ruta_csv)
    actualizado = False

    for pais in paises:
        if pais["nombre"].strip().lower() == nombre:
            print(f"País encontrado: {pais['nombre']}")
            print(f"Población actual: {pais['poblacion']}")
            print(f"Superficie actual: {pais['superficie']} km²")

            nueva_poblacion = validar_poblacion(input("Nueva población: "))
            if nueva_poblacion is None:
                return

            nueva_superficie = validar_superficie(input("Nueva superficie(km²): "))
            if nueva_superficie is None:
                return

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            actualizado = True
            break

    if not actualizado:
        print(f"El país '{nombre}' no fue encontrado.")
        return

    reescribir_archivo(ruta_csv, paises)
    print("País actualizado correctamente")
    
#Buscar un país por nombre (coincidencia parcial o exacta);
def buscar_por_nombre(paises, coincide=False): 
    print("\n---- Buscar país por nombre ----")
    buscar = validar_nombre(input("Ingrese el nombre del país que desea buscar: ").strip().lower())
    if buscar is None:
        return

    paises_encontrados = []

    for pais in paises:
        nombre = pais.get("nombre").lower()
        if coincide:  # Coincidencia exacta
            if nombre == buscar:
                paises_encontrados.append(pais)
        else:  # Coincidencia parcial
            if buscar in nombre:
                paises_encontrados.append(pais)

    if not paises_encontrados:
        print(f"No se encontraron países con el nombre '{buscar}'.")
        return

    print(f"\nSe encontraron {len(paises_encontrados)} país(es) que coinciden con '{buscar}':\n")
    for p in paises_encontrados:
        print(f"- {p['nombre']}; Superficie: {p['superficie']} km²; "
            f"Población: {p['poblacion']}; Continente: {p['continente']}")

#Filtrar paises por continente

def filtrar_por_continente(paises, continente):
    continente = continente.strip().lower()
    paises_filtrados = []
    resultado = ''
    
    if not continente:
        return "No ingresaste ningún continente. Intenta nuevamente."
    
    for pais in paises:
        cont = pais.get("continente").lower()
        if continente == cont:
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

#Filtrar paises por superficie

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