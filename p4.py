from sys import stdin, stdout
import heapq

def dijkstra(graph, start, activities):
    # Distancias inicializadas a un número muy alto
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_gain, current_vertex = heapq.heappop(queue)

        if current_gain > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_gain + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def main():
    # Leer el número de intersecciones y las actividades
    activities = list(map(int, stdin.readline().strip().split()))
    n_intersections = activities[0]
    activities = activities[1:]

    # Leer el número de carreteras
    n_roads = int(stdin.readline().strip())

    # Crear una lista de adyacencia para las carreteras
    graph = [[] for _ in range(n_intersections)]
    for _ in range(n_roads):
        origin, destination = map(int, stdin.readline().strip().split())
        gain = (activities[destination - 1] - activities[origin - 1]) ** 3
        graph[origin - 1].append((destination - 1, gain))

    # Calcular las ganancias mínimas desde la intersección 1 a todas las demás
    min_gains = dijkstra(graph, 0, activities)

    # Leer el número de consultas
    n_queries = int(stdin.readline().strip())

    # Procesar cada consulta
    for i in range(n_queries):
        query = int(stdin.readline().strip())
        gain = min_gains[query - 1]
        if gain < 3 and gain != float('inf'):
            stdout.write('?\n')
        else:
            stdout.write(f'{gain}\n' if gain != float('inf') else '?\n')

if __name__ == "__main__":
    main()
