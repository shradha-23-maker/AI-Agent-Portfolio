# SLE-2: Profiling Report – BFS vs DFS

## Course

02AML204 – Introduction to Artificial Intelligence

## Student Details

- **Name:** Shradha Dhananjay Kumbhar
- **PRN:** 25UAM030
- **Division:** A

## Objective

The objective of this SLE-2 activity is to empirically compare the performance of two uninformed search algorithms:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

Both algorithms are tested on the same graph. Execution time and the number of explored nodes are measured.

## Problem Used

A graph containing 12 nodes is used for the experiment.

- **Start Node:** A
- **Goal Nodes:** A to L

Different goal nodes are tested to observe the best, average, and worst cases.

## Algorithms

### 1. Breadth-First Search (BFS)

BFS explores nodes level by level using a queue.

**File:** `src/bfs.py`

Run:

`python src/bfs.py`

### 2. Depth-First Search (DFS)

DFS explores a path deeply before backtracking. It uses a stack.

**File:** `src/dfs.py`

Run:

`python src/dfs.py`

## Profiling Method

The following methods and tools were used:

- **timeit** – to measure execution time
- **Node counting** – to count explored nodes
- **py-spy** – to generate profiling flame graphs

Each goal node was tested using 1000 runs for time measurement.

## Results

| Metric | BFS | DFS |
|---|---:|---:|
| Best Nodes | 1 | 1 |
| Average Nodes | 6.5 | 6.5 |
| Worst Nodes | 12 | 12 |
| Average Time | 2.1641 µs | 2.3998 µs |
| Worst-case Time | 3.5306 µs | 4.2753 µs |

For this particular graph and experiment, BFS recorded a slightly lower average execution time than DFS. Both algorithms explored the same average number of nodes.

## Py-spy Profiling

### BFS

Profiling file: `bfs_profile.svg`

- Samples: 4
- Errors: 0

### DFS

Profiling file: `dfs_profile.svg`

- Samples: 13
- Errors: 0

The py-spy flame graphs are included as supporting profiling evidence.

## Justification and Analysis

BFS and DFS were tested using the same 12-node graph and the same set of goal nodes. The average number of explored nodes was 6.5 for both algorithms. In this experiment, BFS recorded an average execution time of 2.1641 microseconds, while DFS recorded 2.3998 microseconds. Therefore, BFS showed a slightly lower measured execution time for this particular test. The result depends on the graph structure and test cases used. For larger graphs, the number of nodes explored and execution time can increase significantly.

## AI Contribution Note

AI tools were used to understand the implementation of BFS and DFS, organize the profiling procedure, and improve the explanation of the results. The code was tested and executed locally, and the profiling values were obtained from the student's own runs.

## Conclusion

BFS and DFS were implemented as separate programs and tested on the same graph. Execution time and the number of explored nodes were measured using `timeit`, node counting, and `py-spy`.

For this particular experiment, BFS had a slightly lower average measured execution time than DFS. The measured results are specific to the graph and test cases used.

## Project Files

AI-Agent-Portfolio/

├── src/

│   ├── agent.py

│   ├── bfs.py

│   └── dfs.py

├── bfs_profile.svg

├── dfs_profile.svg

├── SLE2_README.md

├── SLE2_Contribution_Log.md

├── README.md

├── requirements.txt

└── .gitignore