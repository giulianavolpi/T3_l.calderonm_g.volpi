import json
from sys import stdin, stdout
from collections import deque

def bfs(graph, start, goal):
    if start >= len(graph) or goal >= len(graph):
        return False
    if start == goal:
        return True
    visited = set([start])
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current < len(graph):
            for neighbor in graph[current]:
                if neighbor == goal:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return False

def main():
    T = int(stdin.readline().strip())
    for _ in range(T):
        graph = json.loads(stdin.readline().strip())
        start, goal = map(int, stdin.readline().strip().split(','))
        if start < 0 or goal < 0 or start >= len(graph) or goal >= len(graph):
            stdout.write('False\n')
        else:
            result = bfs(graph, start, goal)
            stdout.write(f'{result}\n')

if __name__ == "__main__":
    main()
