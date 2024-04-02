#Se crea el algoritmo de DFS que se utilizará para identificar si un grafo es un árbol o no
import json
from sys import stdin, stdout

def fun_dfs(actual, padre, visitados, list_ady):
    
    visitados.add(actual)
    
    for vecino in list_ady[actual]:
        if vecino not in visitados:
            if not fun_dfs(vecino, actual, visitados, list_ady):
                return False
        elif vecino != padre:
            return False
    return True

def es_arbol(list_ady):
    
    visitados = set()
    
    if fun_dfs(0, -1, visitados, list_ady):
        if len(visitados) == len(list_ady):
            return True
    return False


def main():
    while True:
        try:
            while True:
                num_nodos = stdin.readline().strip()
                if num_nodos.isdigit():
                    break
            num_nodos = int(num_nodos)
            
            lista_de_adyacencia = json.loads(stdin.readline().strip())
            resultado = es_arbol(lista_de_adyacencia)
            print(resultado)
        except EOFError:
            break

if __name__ == "__main__":
    main()