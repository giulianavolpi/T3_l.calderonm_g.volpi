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
    aeropuertos_necesarios = 0
    grafo = {i: [] for i in range(1, N + 1)}
    for a, b in rutas:
        grafo[a].append((b, 1))
        grafo[b].append((a, 1))

    resp = []
    for x, y in demandas:
        if x in ciudades_con_aeropuerto and y in ciudades_con_aeropuerto:
            resp.append(0)
        else:
            distancia = dijkstra(grafo, x)
            if distancia[y] == float('inf'):
                resp.append(-1)
            else:
                for ciudad in range(1, N + 1):
                    if ciudad not in ciudades_con_aeropuerto and distancia[ciudad] != float('inf'):
                        aeropuertos_necesarios += 1
                resp.append(aeropuertos_necesarios)  
    return resp

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



