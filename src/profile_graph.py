from collections import deque


# Larger graph used only for profiling
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
    "H": ["P"],
    "I": ["P"],
    "J": ["Q"],
    "K": ["Q"],
    "L": ["R"],
    "M": ["R"],
    "N": ["S"],
    "O": ["S"],
    "P": ["T"],
    "Q": ["T"],
    "R": ["T"],
    "S": ["T"],
    "T": []
}


def bfs(start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)

            if node == goal:
                return

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


def dfs(start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)

            if node == goal:
                return

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)


start = "A"
goal = "T"

# Run both algorithms repeatedly
for i in range(50000000):
    bfs(start, goal)

for i in range(50000000):
    dfs(start, goal)

print("Profiling workload completed")