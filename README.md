# Actividad-2
Sistema Inteligente de Rutas con Algoritmo A*
Descripción

Este proyecto implementa un sistema inteligente de búsqueda de rutas utilizando el algoritmo A* (A Star) en Python. El sistema encuentra la ruta más eficiente entre estaciones de una red de transporte, considerando los costos de desplazamiento, una función heurística y restricciones como estaciones cerradas por mantenimiento.

Objetivo

Desarrollar una solución basada en Inteligencia Artificial que permita:

Encontrar rutas óptimas entre estaciones.
Reducir el tiempo de búsqueda mediante heurísticas.
Aplicar reglas lógicas para evitar estaciones bloqueadas.
Simular el funcionamiento de sistemas de navegación y transporte inteligente.
Tecnologías utilizadas
Python 3
Librería Heapq (Cola de Prioridad)
Algoritmo de búsqueda A*
Estructura del proyecto
Plain Text
Proyecto
│
├── main.py
├── README.md
Mostrar más líneas
Mapa de estaciones
Plain Text
A
/ \
9 5
/ \
B C
\ /
2 4
\ /
D
/ \
6 3
/ \
E ---1-- F
Mostrar más líneas
Componentes del sistema
Base de conocimiento

Contiene las estaciones y las conexiones entre ellas junto con sus respectivos costos.

Heurística

Representa una estimación de la distancia desde cada estación hacia el destino.

Reglas lógicas

Permite definir estaciones cerradas o restringidas que no deben ser utilizadas durante la búsqueda.

Ejemplo:

Python
bloqueadas = ['E']
Mostrar más líneas
Funcionamiento del algoritmo

El sistema utiliza la fórmula del algoritmo A*:

Plain Text
f(n) = g(n) + h(n)
Mostrar más líneas

Donde:

g(n): costo real recorrido.
h(n): estimación de distancia al destino.
f(n): prioridad total de búsqueda.

La ruta con menor valor de f(n) será explorada primero.

Ejecución del programa

Ejecutar el archivo principal:

Shell
python*main.py
Mostrar más líneas
Ejemplo de ejecución

Entrada:

Plain Text
Ingrese estac*ón inicial: A
Ingrese estación de *estino: B
Mostrar más líneas

Salida:

Plain Text
RU*A ÓPTIMA ENCONTRADA:
A -> B
 
Tiemp* total estimado: 9 minutos
Mostrar más líneas
Ejemplo con estación bloqueada

Configuración:

Python
bloqueadas * ['E']
Mostrar más líneas

Entrada:

Plain Text
Ingr*se estación inicial: F
Ingrese est*ción de destino: E
Mostrar más líneas

Salida:

Plain Text
--- Alerta: Estacion E cerra*a por mantenimiento ---
 
No se pud* encontrar una ruta despejada.
```*
Mostrar más líneas
Conceptos de Inteligencia Artificial aplicados
Sistemas basados en conocimiento.
Búsqueda heurística.
Algoritmo A*.
Sistemas expertos.
Reglas lógicas.
Optimización de rutas.
Resultados

El sistema permite determinar rutas eficientes entre estaciones considerando restricciones operativas y criterios de optimización, simulando escenarios reales de transporte y logística.

Autor

Shirly Alexandra Enciso Ruiz
 Ingeniería de Software
 Actividad Académica: Sistema Inteligente de Rutas con A* y Sistemas Basados en Conocimiento.
