"""

function solve():
    Initialize row queue rq
    Initialize column queue cq

    Enqueue start row (sr) into rq
    Enqueue start column (sc) into cq
    Mark visited[sr][sc] = true

    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    reached_end = false

    while rq is not empty:
        r = rq.dequeue()
        c = cq.dequeue()

        if m[r][c] == 'E':
            reached_end = true
            break

        explore_neighbours(r, c)

        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    if reached_end:
        return move_count
    return -1

function explore_neighbours(r, c):
    for i from 0 to 3:
        rr = r + dr[i]
        cc = c + dc[i]

        if rr < 0 or cc < 0 or rr >= R or cc >= C:
            continue
        if visited[rr][cc] is true:
            continue
        if m[rr][cc] == '#':
            continue

        Enqueue rr into rq
        Enqueue cc into cq
        Mark visited[rr][cc] = true
        nodes_in_next_layer += 1

"""


from collections import deque

# Grid dimensions (R rows, C columns)
R, C = ...  # e.g., R = 5, C = 6

# Input character grid of size R x C (2D list of characters)
# Example: m = [['S', '.', '.', '#', '.', '.'], [...], ...]
m = ...

# Start row and column (position of 'S')
sr, sc = ...

# Directions for north, south, east, west
dr = [-1, +1,  0,  0]
dc = [ 0,  0, +1, -1]

# BFS tracking variables
move_count = 0              # How many steps taken
nodes_left_in_layer = 1     # How many nodes left in current BFS layer
nodes_in_next_layer = 0     # How many will be processed in the next layer
reached_end = False         # Whether we reached the exit ('E')

# Visited tracker: same size as grid, initialized to False
visited = [[False for _ in range(C)] for _ in range(R)]

def solve():
    global move_count, nodes_left_in_layer, nodes_in_next_layer, reached_end

    rq = deque()  # Row queue
    cq = deque()  # Column queue

    # Start BFS from the start position
    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True

    while rq:
        r = rq.popleft()
        c = cq.popleft()

        # Check if we've reached the end
        if m[r][c] == 'E':
            reached_end = True
            break

        # Explore adjacent nodes (up, down, left, right)
        explore_neighbours(r, c, rq, cq)

        # Manage BFS layer tracking
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    if reached_end:
        return move_count
    return -1  # Not reachable

def explore_neighbours(r, c, rq, cq):
    global nodes_in_next_layer

    for i in range(4):  # Check all 4 directions
        rr = r + dr[i]
        cc = c + dc[i]

        # Check bounds
        if rr < 0 or cc < 0 or rr >= R or cc >= C:
            continue

        # Skip visited cells or walls
        if visited[rr][cc]:
            continue
        if m[rr][cc] == '#':
            continue

        # Add to queue and mark as visited
        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True
        nodes_in_next_layer += 1



"""

"""

Absolutely! Let me walk you through how this program works step-by-step, like a story of how it solves the maze. 🧭

⸻

🔍 Goal of the Program

You’re trapped in a 2D dungeon (grid).
There’s a start position ‘S’ and an exit ‘E’, and some walls ‘#’.

The goal is to find:
	•	If escape is possible, and
	•	What is the minimum time (in minutes) it takes to reach ‘E’ from ‘S’

We can only move:
	•	North, South, East, or West
	•	Not diagonally
	•	It takes 1 minute per move

⸻

🧠 High-Level Idea

The program uses a Breadth-First Search (BFS) algorithm to find the shortest path from start (‘S’) to end (‘E’).

Why BFS?

BFS always finds the shortest path in an unweighted graph, like our dungeon (each move takes 1 minute).

⸻

🚀 Step-by-Step Execution

1. Setup
	•	m: the grid with characters 'S', 'E', '.' (open), and '#' (walls)
	•	R and C: number of rows and columns in the grid
	•	sr, sc: the starting row and column (where 'S' is)

We also define:
	•	visited: keeps track of cells we’ve already been to, so we don’t go in circles
	•	move_count: how many steps (minutes) we’ve taken
	•	nodes_left_in_layer: how many nodes are left to explore at the current BFS level (1 at start)
	•	nodes_in_next_layer: how many we’ll visit in the next level
	•	reached_end: tells us if we’ve reached 'E'

⸻

2. Starting the BFS

We use two queues:
	•	One for the row positions
	•	One for the column positions

We add the start position (sr, sc) to both queues, and mark it as visited.

⸻

3. Main BFS Loop (solve() function)

We loop while there’s something in the queue:
	1.	Take a cell from the queue (r, c)
	2.	If it’s 'E' → Done! Set reached_end = True, break
	3.	Else, explore its 4 neighbors (N, S, E, W) using explore_neighbours(r, c)
	4.	After exploring, we decrement nodes_left_in_layer
	5.	If no more nodes left in this layer:
	•	Move to next layer
	•	move_count += 1 (it takes one minute to reach next layer)

⸻

4. Exploring Neighbors (explore_neighbours(r, c) function)

We try to move in all 4 directions:
	•	Check if the new position is inside the grid
	•	Skip it if it’s a wall or already visited
	•	If it’s valid:
	•	Add it to the queues
	•	Mark it as visited
	•	Increase nodes_in_next_layer by 1

⸻

5. Ending the BFS
	•	If we reached 'E', return move_count (time to escape)
	•	If the queue is empty and we never reached 'E', return -1 (no escape)

⸻

✅ Example

Let’s say this is your grid:

S . . #
# # . E

Translates to:

m = [
    ['S', '.', '.', '#'],
    ['#', '#', '.', 'E']
]

The function will:
	•	Start at 'S'
	•	Explore neighbors layer by layer
	•	Find 'E' in the shortest number of moves
	•	Return that count (time)

⸻

🧭 Why It Works
	•	BFS guarantees shortest path
	•	Layer counting (move_count) gives you time in minutes
	•	visited prevents infinite loops or backtracking
	•	Separate row and column queues simulate moving in 2D

⸻

Let me know if you’d like to run a real example with input!

"""


