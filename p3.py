def bfs(grafo, start, end):
    visitados = set()
    distancia = {ciudad: float('inf') for ciudad in grafo}
    distancia[start] = 0
    cola = [start]
    while cola:
        actual = cola.pop(0)
        if actual == end:
            return distancia[end]
        for vecino in grafo[actual]:
            if vecino not in visitados:
                distancia[vecino] = distancia[actual] + 1
                visitados.add(vecino)
                cola.append(vecino)
    return float('inf')

def min_aeropuertos(N, M, K, ciudades_con_aeropuerto, rutas, demandas):
 
    grafo = {i: [] for i in range(1, N + 1)}
    for a, b in rutas:
        grafo[a].append(b)
        grafo[b].append(a)

    resultados = []
    for x, y in demandas:
        if x in ciudades_con_aeropuerto and y in ciudades_con_aeropuerto:
            resultados.append(0)
        else:
            min_aeropuertos = bfs(grafo, x, y)
            if min_aeropuertos == float('inf'):
                resultados.append(-1)
            else:
                resultados.append(min_aeropuertos - 1)
    return resultados

def main():
    X = int(input())
    for caso in range(1, X + 1):
        print(f"Caso #{caso}:")
        N, M, K = map(int, input().split())
        ciudades_con_aeropuerto = set(map(int, input().split()))
        rutas = [tuple(map(int, input().split())) for _ in range(M)]
        Q = int(input())
        demandas = [tuple(map(int, input().split())) for _ in range(Q)]
        
        resultados = min_aeropuertos(N, M, K, ciudades_con_aeropuerto, rutas, demandas)
        
        for resultado in resultados:
            print(resultado)
        print()

if __name__ == "__main__":
    main()
