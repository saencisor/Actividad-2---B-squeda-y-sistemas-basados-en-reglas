# Actividad-2
Sistema Inteligente de Rutas con Algoritmo A*
Descripción

Este proyecto consiste en el desarrollo de un sistema inteligente de búsqueda de rutas utilizando el algoritmo A* (A Star) en Python. El programa permite encontrar la ruta más eficiente entre diferentes estaciones de una red de transporte, considerando los tiempos de desplazamiento, una función heurística y restricciones como estaciones cerradas por mantenimiento.

Objetivo

Desarrollar una solución basada en Inteligencia Artificial que permita calcular rutas óptimas entre estaciones, optimizando el tiempo de recorrido y aplicando reglas lógicas que representen situaciones reales dentro de una red de transporte.

Tecnologías utilizadas
Python 3
Librería Heapq
Algoritmo de búsqueda A*
Mapa de estaciones

La red utilizada en el proyecto está conformada por seis estaciones identificadas con las letras A, B, C, D, E y F. Cada conexión posee un costo que representa el tiempo estimado de recorrido entre estaciones.

A está conectada con B y C.

B está conectada con A y D.

C está conectada con A y D.

D está conectada con B, C, E y F.

E está conectada con D y F.

F está conectada con D y E.

Componentes principales
Base de conocimiento

La base de conocimiento almacena las estaciones y las conexiones disponibles entre ellas. Cada conexión tiene asociado un valor numérico que representa el costo o tiempo de desplazamiento.

Heurística

La heurística es una estimación de la distancia desde cada estación hasta el destino. Esta información permite que el algoritmo tome decisiones más eficientes al seleccionar qué caminos explorar primero.

Reglas lógicas

El sistema incorpora reglas que permiten restringir el acceso a determinadas estaciones. En este proyecto se configuró la estación E como bloqueada para simular una situación de mantenimiento.

Funcionamiento del algoritmo

El programa utiliza el algoritmo A*, uno de los métodos de búsqueda más utilizados en sistemas inteligentes de navegación.

La fórmula utilizada es:

f(n) = g(n) + h(n)

Donde:

g(n): costo real recorrido desde el origen.
h(n): estimación del costo restante hasta el destino.
f(n): valor total utilizado para priorizar las rutas.

El algoritmo evalúa diferentes alternativas y selecciona siempre la ruta con menor costo estimado.

Ejecución del programa

Al iniciar la ejecución, el sistema solicita al usuario una estación de origen y una estación de destino.

Posteriormente:

Verifica que ambas estaciones existan.
Aplica las reglas lógicas definidas.
Ejecuta el algoritmo A*.
Calcula la mejor ruta disponible.
Muestra el recorrido encontrado y el tiempo total estimado.
Ejemplo de uso

Entrada:

Estación inicial: A

Estación destino: B

Resultado:

Ruta óptima encontrada:

A → B

Tiempo total estimado: 9 minutos

Ejemplo con una estación bloqueada

La estación E se encuentra configurada como cerrada por mantenimiento.

Si un usuario intenta encontrar una ruta que requiera pasar por esta estación, el sistema mostrará una alerta indicando que la estación se encuentra bloqueada y buscará rutas alternativas. Si no existe una alternativa disponible, se informará que no fue posible encontrar una ruta despejada.

Conceptos de Inteligencia Artificial aplicados

Durante el desarrollo de este proyecto se aplicaron los siguientes conceptos:

Sistemas basados en conocimiento.
Algoritmos de búsqueda heurística.
Algoritmo A*.
Sistemas expertos.
Reglas lógicas.
Optimización de rutas.
Toma de decisiones basada en prioridades.
Resultados obtenidos

El sistema permite calcular rutas eficientes entre estaciones considerando tanto los costos de desplazamiento como las restricciones operativas definidas. Su funcionamiento demuestra cómo los algoritmos de Inteligencia Artificial pueden ser utilizados para resolver problemas de navegación, logística y transporte de forma eficiente.

Conclusión

El algoritmo A* demostró ser una herramienta eficaz para la búsqueda de rutas óptimas dentro de una red de transporte. Gracias a la utilización de una base de conocimiento, una función heurística y reglas lógicas, el sistema puede encontrar caminos eficientes y adaptarse a escenarios reales como el cierre temporal de estaciones. Este proyecto permite comprender la aplicación práctica de conceptos fundamentales de Inteligencia Artificial en problemas de optimización y planificación de rutas.

Autor

Shirly Alexandra Enciso Ruiz

Ingeniería de Software

Actividad Académica: Sistema Inteligente de Rutas utilizando Algoritmo A* y Sistemas Basados en Conocimiento.

Shirly Alexandra Enciso Ruiz
 Ingeniería de Software
 Actividad Académica: Sistema Inteligente de Rutas con A* y Sistemas Basados en Conocimiento.
