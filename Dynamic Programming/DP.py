"""

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems and solving each subproblem only once, storing its result for future use (a technique known as memoization or tabulation).

Key Characteristics of Dynamic Programming:
	1.	Overlapping Subproblems: The problem can be broken into subproblems which are reused multiple times.
	2.	Optimal Substructure: The solution to the overall problem can be built from the solutions to its subproblems.

Two Main Approaches:
	1.	Top-Down (Memoization):
	•	You solve the main problem recursively.
	•	You store the results of subproblems in a cache (usually an array or dictionary) to avoid recomputation.
	2.	Bottom-Up (Tabulation):
	•	You solve all related subproblems first and use their results to build up solutions to larger problems.
	•	Typically done using iteration and a table (like a 2D array).

Classic Examples:
	•	Fibonacci numbers
	•	Knapsack problem
	•	Longest Common Subsequence (LCS)
	•	Matrix Chain Multiplication
	•	Shortest path in a graph (e.g., Floyd-Warshall algorithm)

 """




"""

Examples for the Dynamic Programming Probrems 

° Calculate the 40th number of the fibonacci sequence 
° Count the number of the different ways to move through a 6X9 grid 
° Given a set of coins,how can we make 27cents in the least number of coins
° Given a set of substrigs, what are the possible ways to construct the stribng "potentpot"

"""
# ---------------------------------------------------------------------------------------------------------

"""

Write a function "fib(n)" that takes in a number as a argument.
The function should return the n-th number of the FIBONACCI sequence.

  
The 1st and 2th number of the sequence is 1.
To generate the next number of the sequence, we sum the previous two.

"""

def fib (n):
  if n <= 2:
    return 1 
  else:
    return fib(n - 1) + fib(n - 2)


"""

0(2^n) time ❌ ==> fib(50) = 2^50 steps ==> 1,125,899,906,842,624

Why? Because:
	•	Every call to fib(n) makes two recursive calls: fib(n-1) and fib(n-2).
	•	This creates a binary tree of recursive calls, and the size of that tree grows exponentially with n.

O(n) space


"""

"""

fib(7)
├── fib(6)
│   ├── fib(5)
│   │   ├── fib(4)
│   │   │   ├── fib(3)
│   │   │   │   ├── fib(2) → 1
│   │   │   │   └── fib(1) → 1
│   │   │   └── fib(2) → 1
│   │   └── fib(3)
│   │       ├── fib(2) → 1
│   │       └── fib(1) → 1
│   └── fib(4)
│       ├── fib(3)
│       │   ├── fib(2) → 1
│       │   └── fib(1) → 1
│       └── fib(2) → 1
└── fib(5)
    ├── fib(4)
    │   ├── fib(3)
    │   │   ├── fib(2) → 1
    │   │   └── fib(1) → 1
    │   └── fib(2) → 1
    └── fib(3)
        ├── fib(2) → 1
        └── fib(1) → 1

"""


def fib(n, memo={}):
    if n in memo:
        return memo[n]	 # Return cached result if available
    if n <= 0:
        return "Input must be a positive integer."
    if n == 1 or n == 2:
        return 1	 # Base cases: fib(1) = fib(2) = 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)	# Compute and store
    return memo[n]



print(fib(10))  # Output: 55
print(fib(50))  # Output: 12586269025 (very fast with memoization!)

"""

How it works:
	•	memo stores results of previous Fibonacci calls.
	•	Instead of recalculating the same values over and over, it looks them up in memo.
"""



# ---------------------------------------------------------------------------------------------------------


"""

Say that you are a traveler on a 2D grid. 
You begin in the top-left corner and your goal is to travel to the bottom-right corner. 
You may only move down or right.
In how many ways can you travel to the goal on a grid with dimensions m * n?
Write a function 'gridTraveler(m, n) that calculates this.

"""


def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)

print(grid_traveler(1, 1))     # 1
print(grid_traveler(2, 3))     # 3
print(grid_traveler(3, 2))     # 3
print(grid_traveler(3, 3))     # 6
print(grid_traveler(18, 18))   # Warning: very slow without memoization!


"""

🚨 Why It’s Slow:
	•	The function recalculates the same values again and again.
	•	For example, grid_traveler(10, 10) ends up recalculating grid_traveler(5, 5) thousands of times.
	•	Each pair (m, n) can be called in many different branches of the recursion tree.

So the number of calls grows like:

T(m, n) = T(m-1, n) + T(m, n-1)

Which leads to a time complexity of approximately:

O(2^{m+n})

That’s why grid_traveler(18, 18) takes so long — it’s making billions of repeated calls.

"""

def grid_traveler(m, n, memo=None):
    if memo is None:
        memo = {}

    key = (m, n)
    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[key]


"""


✅ Time Complexity: O(m × n)

Why?
	•	Each unique pair (m, n) is computed once and stored in the memo dictionary.
	•	Since there are only m × n possible pairs of (m, n), the function makes at most that many recursive calls.
	•	So, the total work done is proportional to the number of unique grid positions.

Conclusion: Time complexity is O(m × n)

⸻

✅ Space Complexity: O(m × n)

Why?
	1.	Memo dictionary stores up to m × n entries.
	2.	Call stack depth (due to recursion) is at most m + n in the worst case — but this is linear, so it doesn’t dominate the total.

Conclusion: Space complexity is also O(m × n)


🧠 Key Insight

Without memoization, these calls would repeat many times, but with memoization, 
each unique (m, n) is calculated once, and reused.


"""

"""

Memoization Recipe
1. Make it work.
• visualize the problem as a tree
• implement the tree using recursion
• test it
2. Make it efficient.
• add a memo object
• add a base case to return memo values
• store return values into the memo


"""





