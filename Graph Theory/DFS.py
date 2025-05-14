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





