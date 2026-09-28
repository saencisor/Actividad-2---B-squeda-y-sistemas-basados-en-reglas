import heapq

# 1. BASE DE CONOCIMIENTO (Mapa de estaciones)
conexiones = {
    'A': {'B': 9, 'C': 5},
    'B': {'A': 9, 'D': 2},
    'C': {'A': 5, 'D': 4},
    'D': {'B': 2, 'C': 4, 'F': 3, 'E': 6},
    'E': {'D': 6, 'F': 1},
    'F': {'D': 3, 'E': 1}
}

# 2. HEURÍSTICA (Estimación al destino B)
h = {'A': 10, 'B': 0, 'C': 7, 'D': 2, 'E': 8, 'F': 5}

# 3. REGLA LÓGICA: Estaciones cerradas
bloqueadas = ['E'] 

def buscar_camino(start, end):
    # (prioridad f, costo g, nodo_actual, camino)
    agenda = [(0 + h[start], 0, start, [])]
    pasados = set()

    while agenda:
        (f, g, nodo, path) = heapq.heappop(agenda)

        if nodo in pasados:
            continue
        
        # Aplicación de la regla lógica
        if nodo in bloqueadas:
            print(f"--- Alerta: Estacion {nodo} cerrada por mantenimiento ---")
            continue

        path = path + [nodo]

        if nodo == end:
            return path, g

        pasados.add(nodo)

        for vecino, peso in conexiones.get(nodo, {}).items():
            if vecino not in pasados:
                nuevo_g = g + peso
                nuevo_f = nuevo_g + h[vecino]
                heapq.heappush(agenda, (nuevo_f, nuevo_g, vecino, path))

    return None, 0


print("--- SISTEMA INTELIGENTE DE RUTAS ---")
print("Estaciones disponibles: A, B, C, D, E, F")

origen = input("Ingrese estación inicial: ").upper()
destino = input("Ingrese estación de destino: ").upper()

# Validar que las estaciones existan para que no se cierre el programa
if origen in conexiones and destino in conexiones:
    resultado, tiempo = buscar_camino(origen, destino)

    if resultado:
        print("\nRUTA ÓPTIMA ENCONTRADA:")
        print(" -> ".join(resultado))
        print(f"Tiempo total estimado: {tiempo} minutos")
    else:
        print("\nNo se pudo encontrar una ruta despejada.")
else:
    print("\nError: Una de las estaciones no existe en el sistema.")