import heapq

def dijkstra(grafo, x):
    distancia = [float('inf')] * (len(grafo) + 1)
    distancia[x] = 0
    cola_prioridad = [(0, x)]

    while cola_prioridad:
        distancia_actual, ciudad_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancia[ciudad_actual]:
            continue

        for vecino in grafo[ciudad_actual]:
            nueva_distancia = distancia_actual + 1
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancia
def min_aeropuertos(N, M, K, ciudades_con_aeropuerto, rutas, demandas):
    # Inicializar el grafo
    grafo = {i: [] for i in range(1, N + 1)}
    for a, b in rutas:
        grafo[a].append(b)
        grafo[b].append(a)

    respuestas = []
    for demanda in demandas:
        x, y = demanda
        if x == y:
            # Si el origen y destino son iguales, no se necesitan aeropuertos adicionales.
            respuestas.append(0)
            continue

        distancia = dijkstra(grafo, x)
        if distancia[y] == float('inf'):
            # Si no hay ruta posible, la demanda no puede ser satisfecha.
            respuestas.append(-1)
            continue

        # Reconstruir la ruta mínima
        ruta_minima = []
        ciudad_actual = y
        while ciudad_actual != x:
            ruta_minima.append(ciudad_actual)
            for vecino in grafo[ciudad_actual]:
                if distancia[ciudad_actual] == distancia[vecino] + 1:
                    ciudad_actual = vecino
                    break
        ruta_minima.append(x)  # Agregar la ciudad de origen al final de la ruta mínima
        ruta_minima.reverse()  # Invertir la ruta para que empiece desde el origen

        # Contar solo las ciudades que necesitan un aeropuerto nuevo.
        aeropuertos_necesarios = sum(1 for ciudad in ruta_minima if ciudad not in ciudades_con_aeropuerto)
        respuestas.append(aeropuertos_necesarios)

    return respuestas

def main():
    X = int(input())
    for caso in range(1, X + 1):
        print(f"Caso {caso}:")
        N, M, K = map(int, input().split())
        ciudades_con_aeropuerto = set(map(int, input().split()))
        rutas = [tuple(map(int, input().split())) for _ in range(M)]
        Q = int(input())
        demandas = [tuple(map(int, input().split())) for _ in range(Q)]
        
        resp = min_aeropuertos(N, M, K, ciudades_con_aeropuerto, rutas, demandas)
        
        for resultado in resp:
            print(resultado)
        print()

if __name__ == "__main__":
    main()
