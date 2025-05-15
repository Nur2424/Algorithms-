"""
Global/class scope variables:
n = number of nodes in the graph
g = adjacency list representing unweighted graph

function bfs(s, e):
    # Do a BFS starting from node s
    prev = solve(s)
    
    # Return reconstructed path from s to e
    return reconstructPath(s, e, prev)

function solve(s):
    q = queue data structure
    q.enqueue(s)
    
    visited = [false, false, ..., false]  # size n
    visited[s] = true
    
    prev = [null, null, ..., null]  # size n
    
    while q is not empty:
        node = q.dequeue()
        neighbours = g[node]
        
        for next in neighbours:
            if not visited[next]:
                q.enqueue(next)
                visited[next] = true
                prev[next] = node
    
    return prev

function reconstructPath(s, e, prev):
    path = []
    at = e
    while at is not null:
        path.add(at)
        at = prev[at]
    
    path.reverse()
    
    if path[0] == s:
        return path
    return []

    """

from collections import deque

# Global/class scope variables
n = 0  # number of nodes
g = []  # adjacency list

def bfs(s, e):
    prev = solve(s)
    return reconstruct_path(s, e, prev)

def solve(s):
    q = deque()
    q.append(s)

    visited = [False] * n
    visited[s] = True

    prev = [None] * n

    while q:
        node = q.popleft()
        for neighbor in g[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                prev[neighbor] = node

    return prev

def reconstruct_path(s, e, prev):
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = prev[at]
    
    path.reverse()

    if path and path[0] == s:
        return path
    return []
"""

# Example usage

n = 6
g = [
    [1, 2],     # Node 0
    [0, 3],     # Node 1
    [0, 4],     # Node 2
    [1, 5],     # Node 3
    [2],        # Node 4
    [3]         # Node 5
]
------------------
      0
     / \
    1   2
    |    \
    3     4
    |
    5

_________________

start = 0
end = 5

path = bfs(start, end)
print("Shortest path from", start, "to", end, "is:", path)

# OUTPUT: Shortest path from 0 to 5 is: [0, 1, 3, 5]

"""


"""

Great! Let’s walk through this Breadth-First Search (BFS) implementation that finds the shortest path in an unweighted graph from a start node s to an end node e.

⸻

🔍 What the Code Does

This code performs BFS to find the shortest path (in terms of number of edges) from node s to node e. It does this in three parts:

1. bfs(s, e)
	•	This is the main function you call.
	•	It runs solve(s) to perform BFS starting from node s.
	•	Then it uses reconstruct_path(s, e, prev) to build the actual path from s to e using the prev array.

⸻

2. solve(s)
	•	Runs BFS from the start node s.
	•	Tracks:
	•	visited: nodes that have already been visited.
	•	prev: an array to keep track of the previous node for each node visited.
	•	This helps in reconstructing the path later.

How it works:
	•	Start with the queue containing s.
	•	While the queue is not empty:
	•	Dequeue a node.
	•	Explore its neighbors.
	•	For every unvisited neighbor:
	•	Mark it as visited.
	•	Add it to the queue.
	•	Set prev[neighbor] = current node.

This effectively builds a shortest-path tree rooted at s.

⸻

3. reconstruct_path(s, e, prev)
	•	Traces back from node e to s using the prev array.
	•	Builds the path in reverse order and then reverses it to get the correct direction.

# path = []
# at = e
# while at is not None:
#     path.append(at)
#     at = prev[at]
# path.reverse()

	•	If a path exists, path[0] should be s.
	•	If not, return an empty list.

⸻

🧪 Example Breakdown

n = 6
g = [
    [1, 2],     # 0
    [0, 3],     # 1
    [0, 4],     # 2
    [1, 5],     # 3
    [2],        # 4
    [3]         # 5
]

start = 0
end = 5

Graph structure:

      0
     / \
    1   2
    |    \
    3     4
    |
    5

BFS from 0:
	•	Queue: [0]
	•	Visit 0 → enqueue [1, 2] → prev[1] = 0, prev[2] = 0
	•	Visit 1 → enqueue [3] → prev[3] = 1
	•	Visit 2 → enqueue [4] → prev[4] = 2
	•	Visit 3 → enqueue [5] → prev[5] = 3
	•	Done

Reconstruct path from 5 to 0:
	•	5 ← 3 ← 1 ← 0
	•	Final path: [0, 1, 3, 5]

⸻

✅ Output:

Shortest path from 0 to 5 is: [0, 1, 3, 5]


⸻

📌 Summary
	•	BFS guarantees shortest path in unweighted graphs.
	•	The prev[] array helps you reconstruct the path.
	•	Time complexity: O(V + E) where V is the number of nodes and E is the number of edges.

Let me know if you want to modify it for all shortest paths, path existence, or a directed graph!

"""
