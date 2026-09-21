from sle2_bfs_dfs import bfs

start = "A"
goal = "L"

# Run BFS many times so py-spy has enough time to sample it
for i in range(100000000):
    bfs(start, goal)

print("BFS profiling completed")