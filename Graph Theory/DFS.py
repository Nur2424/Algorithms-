"""
// Global variables
n = number of nodes in the graph  
g = adjacency list representing the graph  
count = 0  
components = array of size n  // Stores component IDs  
visited = array of size n     // Tracks visited nodes (initialized to false)  

// Main function to find connected components
function findComponents():
    for i = 0 to n-1:
        if not visited[i]:
            count += 1
            dfs(i)
    return (count, components)

// Depth-First Search (DFS) subroutine
function dfs(at):
    visited[at] = true
    components[at] = count
    for next in g[at]:
        if not visited[next]:
            dfs(next)
"""

# Global or class scope variables
n = 0  # number of nodes in the graph
g = []  # adjacency list representing graph
count = 0  # component counter
components = []  # stores component number for each node
visited = []  # visited flag for each node

def find_components():
    global count, visited, components
    count = 0
    visited = [False] * n
    components = [-1] * n

    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    
    return count, components

def dfs(at):
    visited[at] = True
    components[at] = count

    for next_node in g[at]:
        if not visited[next_node]:
            dfs(next_node)

"""
Example usage

n = 5
g = [
    [1, 2],    # Node 0 is connected to 1 and 2
    [0, 2],    # Node 1 is connected to 0 and 2
    [0, 1],    # Node 2 is connected to 0 and 1
    [4],       # Node 3 is connected to 4
    [3]        # Node 4 is connected to 3
]

component_count, component_ids = find_components()
print("Number of components:", component_count)
print("Component IDs:", component_ids)

Number of components: 2
Component IDs: [1, 1, 1, 2, 2]

"""

"""

Absolutely! Let’s go step by step and explain how the code finds connected components in an undirected graph using Depth-First Search (DFS).

⸻

What Are Connected Components?

In an undirected graph, a connected component is a group of nodes where each node is reachable from any other node in the same group. If a node cannot be reached from another, it belongs to a different component.

⸻

Code Overview

The code is split into two main parts:
	1.	find_components() — the main function to find all connected components.
	2.	dfs(at) — a helper function that performs DFS from a given node.

Additionally, there are some global variables:
	•	n – number of nodes
	•	g – adjacency list (each node points to a list of connected nodes)
	•	count – current component ID
	•	components – array that keeps track of which component each node belongs to
	•	visited – array to mark visited nodes

⸻

Step-by-Step Execution

Initial Setup

Before calling find_components(), you define:

n = 5
g = [
    [1, 2],    # Node 0
    [0, 2],    # Node 1
    [0, 1],    # Node 2
    [4],       # Node 3
    [3]        # Node 4
]

So you have:
	•	5 nodes
	•	Node 0, 1, 2 are all interconnected (Component 1)
	•	Node 3 and 4 are connected to each other but not to any of the others (Component 2)

⸻

1. find_components() Function

This loops over all nodes:

for i in range(n):
    if not visited[i]:
        count += 1
        dfs(i)

	•	If a node hasn’t been visited, that means it’s part of a new component.
	•	Increment count to assign a new component ID.
	•	Call dfs(i) to explore all nodes in this component.

⸻

2. dfs(at) Function

This is standard DFS:

visited[at] = True
components[at] = count
for next_node in g[at]:
    if not visited[next_node]:
        dfs(next_node)

	•	Mark current node at as visited.
	•	Assign it the current component ID (count).
	•	Visit all its neighbors recursively.

⸻

What Happens in Your Example
	1.	Start at node 0 (not visited)
	•	count = 1
	•	Run dfs(0): visits 1 and 2 (since they’re all connected)
	•	All of nodes 0, 1, 2 are assigned component 1
	2.	Move to node 1 → already visited → skip
	3.	Node 2 → already visited → skip
	4.	Node 3 (not visited)
	•	count = 2
	•	Run dfs(3): visits 4
	•	Nodes 3 and 4 are assigned component 2

⸻

Final Result

component_count = 2
component_ids = [1, 1, 1, 2, 2]

	•	Two connected components
	•	Nodes 0, 1, 2 belong to component 1
	•	Nodes 3, 4 belong to component 2

⸻

Conclusion

This is a classic way to find connected components in an undirected graph using DFS. It’s efficient and works well for sparse graphs represented as an adjacency list.

Let me know if you want the same for a directed graph or a non-recursive DFS version!


"""
