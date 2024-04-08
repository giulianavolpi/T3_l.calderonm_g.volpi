from collections import deque

def construir_grafo(N, M, rutas):
   grafo = {i: set() for i in range(1, N + 1)}
   for a, b in rutas:
       grafo[a].add(b)
       grafo[b].add(a)
   return grafo

def bfs(grafo, inicio, destino, ciudades_con_aeropuerto):
   visitados = set()
   cola = deque([(inicio, 0 if inicio in ciudades_con_aeropuerto else 1)])
   while cola:
       ciudad_actual, aeropuertos_necesarios = cola.popleft()
       if ciudad_actual == destino:
           if destino not in ciudades_con_aeropuerto:
               aeropuertos_necesarios += 1
           return aeropuertos_necesarios
       if ciudad_actual not in visitados:
           visitados.add(ciudad_actual)
           for vecino in grafo[ciudad_actual]:
               if vecino not in visitados:
                   cola.append((vecino, aeropuertos_necesarios))
   return -1

def min_aeropuertos(N, M, K, ciudades_con_aeropuerto, rutas, demandas):
   grafo = construir_grafo(N, M, rutas)
   resultados = []
   for demanda in demandas:
       x, y = demanda
       resultados.append(bfs(grafo, x, y, set(ciudades_con_aeropuerto)))
   return resultados

def main():
   X = int(input())
   for caso in range(1, X + 1):
       N, M, K = map(int, input().split())
       ciudades_con_aeropuerto = list(map(int, input().split()))
       rutas = [tuple(map(int, input().split())) for _ in range(M)]
       Q = int(input())
       demandas = [tuple(map(int, input().split())) for _ in range(Q)]
       
       resultados = min_aeropuertos(N, M, K, ciudades_con_aeropuerto, rutas, demandas)
       print(f"Caso {caso}:")
       for resultado in resultados:
           print(resultado)
       print()

if __name__ == "__main__":
   main()





# Se decicidió dejar la implementación por Dijkstra ya que este algoritmo tiene un sentido teórico.
# Se buscó implementar Dijkstra junto con un contador de las ciudades visitadas que no tengan aeropuerto. 
# Sin embargo el algoritmo con bfs resuelve de mejor manera el problema.

# import heapq

# def dijkstra(grafo, x):
#     distancia = [float('inf')] * (len(grafo) + 1)
#     distancia[x] = 0
#     cola_prioridad = [(0, x)]

#     while cola_prioridad:
#         distancia_actual, ciudad_actual = heapq.heappop(cola_prioridad)

#         if distancia_actual > distancia[ciudad_actual]:
#             continue

#         for vecino in grafo[ciudad_actual]:
#             nueva_distancia = distancia_actual + 1
#             if nueva_distancia < distancia[vecino]:
#                 distancia[vecino] = nueva_distancia
#                 heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

#     return distancia

# def main():
  
#     N = int(input())
#     M = int(input())
#     grafo = {i: [] for i in range(1, N + 1)}

#     for _ in range(M):
#         a, b = map(int, input().split())
#         grafo[a].append(b)
#         grafo[b].append(a)

#     x, y = map(int, input().split())
#     distancia = dijkstra(grafo, x)

#     if distancia[y] == float('inf'):
#         print(-1)
#     else:
#         print(distancia[y])

# if __name__ == '__main__':
#     main()