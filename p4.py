def dijkstra(actividades, grafo, start):
    n = len(actividades) - 1
    distancia = [float('inf')] * (n + 1)
    distancia[start] = 0
    cola = [(0, start)]
    import heapq
    while cola:
        distancia_actual, actual = heapq.heappop(cola)
        if distancia_actual > distancia[actual]:
            continue
        
        for vecino in grafo[actual]:
            peso = abs(actividades[vecino] - actividades[actual]) ** 3
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
    
    return distancia

def calcular_ganancias(n, actividades, rutas, consultas):
    grafo = {i: [] for i in range(1, n + 1)}
    for a, b in rutas:
        grafo[a].append(b)
    
    distancia = dijkstra(actividades, grafo, 1)
    resultados = []
    for consulta in consultas:
        ganancia = distancia[consulta]
        if ganancia == float('inf'):
            resultados.append('?')
        else:
            resultados.append(int(ganancia))
    
    return resultados
def main():
    caso = 1
    entrada = input().split()
    while entrada:
        n = int(entrada[0])
        actividades = [0] + list(map(int, entrada[1:]))
        r = int(input())
        rutas = [tuple(map(int, input().split())) for _ in range(r)]
        q = int(input())
        consultas = [int(input()) for _ in range(q)]
        
        resultados = calcular_ganancias(n, actividades, rutas, consultas)
        print(f"Set #{caso}")
        for resultado in resultados:
            print(resultado)
        caso += 1
        try:
            entrada = input().split()
        except EOFError:
            break

if __name__ == "__main__":
    main()
