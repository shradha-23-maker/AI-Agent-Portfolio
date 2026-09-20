from collections import deque
import time

# Graph
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": ["G"],
    "G": []
}


# BFS
def bfs(start, goal):
    queue = deque([start])
    visited = []
    nodes = 0

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            nodes += 1

            if node == goal:
                return visited, nodes

            for neighbour in graph[node]:
                queue.append(neighbour)

    return visited, nodes


# DFS
def dfs(start, goal):
    stack = [start]
    visited = []
    nodes = 0

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            nodes += 1

            if node == goal:
                return visited, nodes

            for neighbour in graph[node]:
                stack.append(neighbour)

    return visited, nodes


# Start and goal
start = "A"
goal = "G"

# BFS timing
start_time = time.perf_counter()

for i in range(10000):
    bfs_result, bfs_nodes = bfs(start, goal)

bfs_time = time.perf_counter() - start_time


# DFS timing
start_time = time.perf_counter()

for i in range(10000):
    dfs_result, dfs_nodes = dfs(start, goal)

dfs_time = time.perf_counter() - start_time


# Display results
print("===== BFS vs DFS =====")

print("\nBFS")
print("Visited:", bfs_result)
print("Nodes explored:", bfs_nodes)
print("Time:", bfs_time, "seconds")

print("\nDFS")
print("Visited:", dfs_result)
print("Nodes explored:", dfs_nodes)
print("Time:", dfs_time, "seconds")