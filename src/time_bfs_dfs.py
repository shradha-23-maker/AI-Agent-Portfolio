import timeit
from sle2_bfs_dfs import bfs, dfs

start = "A"
goal = "L"

# Measure BFS execution time
bfs_time = timeit.timeit(
    lambda: bfs(start, goal),
    number=10000
)

# Measure DFS execution time
dfs_time = timeit.timeit(
    lambda: dfs(start, goal),
    number=10000
)

# Get node counts
bfs_nodes = bfs(start, goal)
dfs_nodes = dfs(start, goal)

print("===== BFS vs DFS Timing =====")
print("BFS Nodes Explored:", bfs_nodes)
print("BFS Total Time for 10000 runs:", bfs_time, "seconds")
print("BFS Average Time:", bfs_time / 10000, "seconds")

print()

print("DFS Nodes Explored:", dfs_nodes)
print("DFS Total Time for 10000 runs:", dfs_time, "seconds")
print("DFS Average Time:", dfs_time / 10000, "seconds")