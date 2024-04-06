import heapq

def dijkstra(grafo, start):
    distancia = {ciudad: float('inf') for ciudad in grafo}
    distancia[start] = 0
    cola = [(0, start)]
    while cola:
        distancia_actual, actual = heapq.heappop(cola)
        if distancia_actual > distancia[actual]:
            continue
        for vecino, peso in grafo[actual]:
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
    return distancia

def min_aeropuertos(N, M, K, ciudades_con_aeropuerto, rutas, demandas):
    # Inicializar el grafo
    grafo = {i: [] for i in range(1, N + 1)}
    for a, b in rutas:
        grafo[a].append((b, 1))
        grafo[b].append((a, 1))

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

        # Calcular aeropuertos necesarios considerando ciudades sin aeropuerto en la ruta mínima
        ciudades_en_ruta = set()
        ciudad_actual = y
        while ciudad_actual != x:
            for vecino, _ in grafo[ciudad_actual]:
                if distancia[ciudad_actual] == distancia[vecino] + 1:
                    ciudades_en_ruta.add(ciudad_actual)
                    ciudad_actual = vecino
                    break

        # Contar solo las ciudades que necesitan un aeropuerto nuevo.
        aeropuertos_necesarios = sum(1 for ciudad in ciudades_en_ruta if ciudad not in ciudades_con_aeropuerto)
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
