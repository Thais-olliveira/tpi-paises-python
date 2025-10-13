import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import core.lectura_csv
import core.filtros 
dados = core.lectura_csv.cargar_paises("../data/paises_dataset.csv")

print("Iniciando pruebas de los filtros")

# print("Cargan datos")
# print(dados)

# print("Busca por nombre")   
# retorno_filtro = core.filtros.buscar_por_nombre(dados, "brasil")
# print(retorno_filtro)

# print("Filtrando por continente")   
# retorno_filtro = core.filtros.filtrar_por_continente(dados, "América del Norte")
# print(retorno_filtro)

# print("Filtrando por paises con poblacion entre (Min - Max)")
# retorno_filtro = core.filtros.filtrar_por_poblacion(dados, 0, 1000)
# print(retorno_filtro)

# print("Filtrando por paises con area entre (Min - Max)")
# retorno_filtro = core.filtros.filtrar_por_superficie(dados, 0, 100)
# print(retorno_filtro)

print("Iniciando pruebas de los estadisticas")
