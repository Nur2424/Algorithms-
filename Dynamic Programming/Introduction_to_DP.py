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
























