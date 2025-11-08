import core.lectura_csv
import core.filtros
import core.estadisticas
import core.ordenamientos


RUTA_CSV = "data/paises_dataset.csv"

def submenu_ordenamientos(paises):
    while True:
        print("\n---- ORDENAMIENTOS ----")
        print("1. Ordenar por nombre (A-Z)")
        print("2. Ordenar por población (menor a mayor)")
        print("3. Ordenar por superficie ascendente (menor a mayor)")
        print("4. Ordenar por superficie descendente (mayor a menor)")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            core.ordenamientos.ordenar_por_nombre(paises)
        
        elif opcion == "2":
            core.ordenamientos.ordenar_por_poblacion(paises)

        elif opcion == "3":
            core.ordenamientos.ordenar_por_superficie_ascendente(paises)
        
        elif opcion == "4":
            core.ordenamientos.ordenar_por_superficie_descendente(paises)

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu():
    paises = core.lectura_csv.cargar_paises()

    if not paises:
        print("No se pudieron cargar los países. Verificá el archivo CSV.")
        return

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar país")
        print("2. Actualizar país")
        print("3. Buscar país por nombre")
        print("4. Filtrar por continente")
        print("5. Filtrar por población")
        print("6. Filtrar por superficie")
        print("7. Estadísticas")
        print("8. Ordenamientos")
        print("9. Salir")

        opcion = input("Elija una opción: ").strip()

        if opcion == '1':
            core.filtros.agregar_pais(RUTA_CSV)
            paises = core.lectura_csv.cargar_paises()
        
        elif opcion == '2':
            core.filtros.actualizar_pais(RUTA_CSV)
            paises = core.lectura_csv.cargar_paises()
        
        elif opcion == '3':
            core.filtros.buscar_por_nombre(paises)

        elif opcion == '4':
            continente = core.filtros.elegir_continente_desde_lista()
            if continente is not None:
                print(core.filtros.filtrar_por_continente(paises, continente))

        elif opcion == '5':
            min_pop = input("Población mínima: ")
            max_pop = input("Población máxima: ")
            print(core.filtros.filtrar_por_poblacion(paises, min_pop, max_pop))

        elif opcion == '6':
            min_area = input("Superficie mínima: ")
            max_area = input("Superficie máxima: ")
            print(core.filtros.filtrar_por_superficie(paises, min_area, max_area))

        elif opcion == '7':
            print("\n---- Estadísticas ---")
            core.estadisticas.mayor_menor_poblacion(paises)
            print(f"Promedio de población: {core.estadisticas.promedio_poblacion(paises):,.0f}")
            print(f"Promedio de superficie: {core.estadisticas.promedio_superficie(paises):,.0f}")
            core.estadisticas.cantidad_paises_continente(paises)

        elif opcion == '8':
            submenu_ordenamientos(paises)
            
        elif opcion == '9':
            print("Saliendo del programa... ")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
            
menu()


