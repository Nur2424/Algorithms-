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





