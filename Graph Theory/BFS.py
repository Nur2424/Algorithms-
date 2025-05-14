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

start = 0
end = 5

path = bfs(start, end)
print("Shortest path from", start, "to", end, "is:", path)

# OUTPUT: Shortest path from 0 to 5 is: [0, 1, 3, 5]
