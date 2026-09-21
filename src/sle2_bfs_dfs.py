from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": ["K"],
    "H": ["L"],
    "I": ["L"],
    "J": ["L"],
    "K": ["L"],
    "L": []
}

def bfs(start, goal):
    queue = deque([start])
    visited = set()
    nodes_explored = 0

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            nodes_explored += 1

            if node == goal:
                return nodes_explored

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return nodes_explored


def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_explored = 0

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            nodes_explored += 1

            if node == goal:
                return nodes_explored

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return nodes_explored


if __name__ == "__main__":
    start = "A"
    goal = "L"

    print("===== BFS vs DFS =====")

    print("\nBFS")
    for i in range(10000):
        bfs_nodes = bfs(start, goal)

    print("Nodes Explored:", bfs_nodes)

    print("\nDFS")
    for i in range(10000):
        dfs_nodes = dfs(start, goal)

    print("\n===== Final Result =====")
    print("BFS Nodes Explored:", bfs_nodes)
    print("DFS Nodes Explored:", dfs_nodes)