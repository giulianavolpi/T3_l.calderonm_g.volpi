def bellman_ford(actividades, grafo, start):
    n = len(actividades) - 1
    distancia = [float('inf')] * (n + 1)
    distancia[start] = 0
    
    # Relajar las aristas n - 1 veces
    for _ in range(n):
        for actual in range(1, n + 1):
            for vecino in grafo[actual]:
                peso = (actividades[vecino] - actividades[actual]) ** 3
                if peso < 0:
                    continue  # Ignoramos pesos negativos, como se hacía antes
                if distancia[actual] + peso < distancia[vecino]:
                    distancia[vecino] = distancia[actual] + peso
    
    # Comprobar ciclos de peso negativo (no necesario para este problema, pero es parte del algoritmo)
    for actual in range(1, n + 1):
        for vecino in grafo[actual]:
            peso = (actividades[vecino] - actividades[actual]) ** 3
            if peso < 0:
                continue
            if distancia[actual] + peso < distancia[vecino]:
                print("Ciclo de peso negativo encontrado")
                return None
    
    return distancia

def calcular_ganancias(n, actividades, rutas, consultas):
    grafo = {i: [] for i in range(1, n + 1)}
    for a, b in rutas:
        grafo[a].append(b)
    distancia = bellman_ford(actividades, grafo, 1)
    resultados = []
    for consulta in consultas:
        ganancia = distancia[consulta]
        if ganancia == float('inf') or ganancia < 3:
            resultados.append('?')
        else:
            resultados.append(int(ganancia))
    
    return resultados

def main():
    caso = 1
    while True:
        try:
            entrada = input().split()
            if not entrada:
                break
            n = int(entrada[0])
            if n == 0:
                break
            actividades = [0] + list(map(int, entrada[1:n+1]))
            r = int(input())
            rutas = [tuple(map(int, input().split())) for _ in range(r)]
            q = int(input())
            consultas = [int(input()) for _ in range(q)]
            
            resultados = calcular_ganancias(n, actividades, rutas, consultas)
            print(f"Set #{caso}")
            for resultado in resultados:
                print(resultado)
            caso += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()
