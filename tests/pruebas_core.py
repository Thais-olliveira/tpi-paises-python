import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import core.lectura_csv
import core.filtros 
import core.estadisticas
import core.ordenamientos

dados = core.lectura_csv.cargar_paises()


print("Cargan datos")
print(dados)

print("Pruebas de los filtros")

# print("Agregar un nuevo pais")
# retorno_filtro = core.filtros.agregar_pais("data/paises_dataset.csv")

# print("Actualizar pais")
# retorno_filtro = core.filtros.actualizar_pais("data/paises_dataset.csv")

# print("Busca por nombre")
# retorno_filtro = core.filtros.buscar_por_nombre(dados)

# print("Filtrando por continente")   
# retorno_filtro = core.filtros.filtrar_por_continente(dados, "América del Norte")
# print(retorno_filtro)

# print("Filtrando por paises con poblacion entre (Min - Max)")
# retorno_filtro = core.filtros.filtrar_por_poblacion(dados, 0, 1000)
# print(retorno_filtro)

# print("Filtrando por paises con area entre (Min - Max)")
# retorno_filtro = core.filtros.filtrar_por_superficie(dados, 0, 100)
# print(retorno_filtro)

print("Pruebas de estadisticas")

# print("Promedio Poblacion")
# retorno_estadistica = core.estadisticas.promedio_poblacion(dados)
# print(retorno_estadistica)
# print("Promedio de la población total:", retorno_estadistica)

# print("Promedio Superficie")
# retorno_estadistica = core.estadisticas.promedio_superficie(dados)
# print(retorno_estadistica)
# print("Promedio de la superficie total:", retorno_estadistica)

# print("Cantidad paises por continente")
# retorno_estadistica = core.estadisticas.cantidad_paises_continente(dados)

print("Prubas de ordenamiento")

# print("Ordenar por nombre")
# retorno_ordenamiento = core.ordenamientos.ordenar_por_nombre(dados)

# print("Ordenar por poblacion")
# retorno_ordenamiento = core.ordenamientos.ordenar_por_poblacion(dados)

# print("Ordenar por poblacion ascendente")
# retorno_ordenamiento = core.ordenamientos.ordenar_por_superficie_ascendente(dados)

# print("Ordenar por poblacion descendente")
# retorno_ordenamiento = core.ordenamientos.ordenar_por_superficie_descendente(dados)