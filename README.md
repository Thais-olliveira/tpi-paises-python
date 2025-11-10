## Trabajo Práctico Integrador - Gestión de Datos de Países en Python

**Programación I – Comisión 14**  
**Alumnas:** Thais Alvim / Constanza Jazmín Jiménez  


## 🧾 Descripción del programa
Este trabajo fue desarollado como parte del trabajo práctico integrador y permite gestionar información sobre países a partir de un archivo CSV con datos como nombre, superficie, población y continente.


## ⚙️ Funcionalidades principales
- Agregar y actualizar países;
- Buscar por nombre;
- Filtrar por continente, población o superficie;
- Calcular estadísticas generales;
- Ordenar países según distintos criterios.

## 🗂️ Estructura de archivos 
Los archivos principales consisten en los siguientes:
1) menu.py: contiene el menú principal y el flujo general del programa.
2) lectura_csv.py: lee el archivo CSV y carga los datos en una lista de diccionarios.
3) filtros.py: permite buscar, agregar, actualizar o filtrar países según distintos criterios.
4) estadísticas.py: calcula estadísticas (mayor/menor población, promedios, cantidad por continente).
5) ordenamientos.py: ordena los países por nombre, población o superficie.
6) data/paises_dataset.csv: archivo con los datos base de los países.

La ejecución del programa se da en tres pasos: primero se asegura que el archivo paises_dataset.csv esté dentro de la carpeta data. Segundo, se ejecuta el programa principal desde la terminal o VIsual Studio Code y tercero se siguen las opciones del menú que aparecen en pantalla.

[Diagrama de flujo general del sistema](diagramadeflujo.jpeg)

[Documentación Teórica del Proyecto](TPI-ProgramaciónI-Grupo84-Thaís-Constanza.pdf)

## 🧠 Ejemplo de entradas y salidas 

Entrada:
Opción elegida: 8 → 1. Ordenar por nombre (A-Z)

Salida:
Países ordenados alfabéticamente:
- Andorra
- Argentina
- Australia
- Brasil
- Canadá
- Chile
- China
- Egipto
- Estados Unidos
- Japón
- Nueva Zelanda
- Sudáfrica

## 👥 Participación de los integrantes

**Thais Alvim**  Funciones de filtrado, estadísticas y ordenamiento.
**Constanza Jazmín Jiménez** Carga de datos desde CSV, Implementación del menú principal y del submenú de ordenamiento y validación de entradas.

