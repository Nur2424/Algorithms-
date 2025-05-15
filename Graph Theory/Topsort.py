"""

function dfs(at, V, visitedNodes, graph):
    V[at] = true
    edges = graph.getEdgesOutFromNode(at)
    for edge in edges:
        if V[edge.to] == false:
            dfs(edge.to, V, visitedNodes, graph)
    visitedNodes.add(at)

function topsort(graph):
    N = graph.numberOfNodes()
    V = [false, ..., false]  # Length N
    ordering = [0, ..., 0]   # Length N
    i = N - 1  # Start filling ordering from the end

    for at = 0 to N - 1:
        if V[at] == false:
            visitedNodes = []
            dfs(at, V, visitedNodes, graph)
            for nodeId in visitedNodes:
                ordering[i] = nodeId
                i = i - 1

    return ordering


    """

"""

That’s completely normal — topological sort can be tricky to turn into working code at first! Let’s build it step-by-step together. Below is a super simplified and readable version, followed by an interactive breakdown so you can really see what’s happening.

⸻

✅ Step-by-Step Python Code for Topological Sort Using DFS
"""
def dfs(node, visited, stack, graph):
    # Mark the current node as visited
    visited[node] = True

    # Visit all neighbors
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack, graph)

    # Add the node to the stack after visiting neighbors
    stack.append(node)


def topological_sort(graph):
    n = len(graph)  # number of nodes
    visited = [False] * n
    stack = []  # stores the topological order in reverse

    for node in range(n):
        if not visited[node]:
            dfs(node, visited, stack, graph)

    # reverse the stack to get the correct order
    stack.reverse()
    return stack

"""
⸻

🧪 Example Input

graph = [
    [1, 2],  # 0 -> 1, 2
    [3],     # 1 -> 3
    [3],     # 2 -> 3
    []       # 3 has no neighbors
]

order = topological_sort(graph)
print("Topological Order:", order)

Expected Output (one of the valid orders):

Topological Order: [0, 2, 1, 3]


⸻

🧠 What Each Part Does
	•	graph: adjacency list (graph[u] = [v1, v2, ...]) means u → v1, u → v2, …
	•	visited: avoids revisiting nodes
	•	stack: records nodes after all their dependencies are processed
	•	stack.reverse(): because in DFS, we add the node after its children (post-order)

⸻

💡 Tip for Learning

To practice:
	1.	Draw a small DAG (like 4–5 nodes)
	2.	Convert it into an adjacency list
	3.	Walk through the code manually or with print()s at each step


"""





