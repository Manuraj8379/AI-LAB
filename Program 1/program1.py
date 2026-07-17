from collections import deque

# ---------------- DFS ----------------
def dfs(graph, start, visited=None, order=None):

    if visited is None:
        visited = set()

    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, order)

    return order


# ---------------- BFS ----------------
def bfs(graph, start):

    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


# ---------------- Graph ----------------
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# ---------------- Output ----------------
print("DFS Traversal:", dfs(graph, 'A'))
print("BFS Traversal:", bfs(graph, 'A'))