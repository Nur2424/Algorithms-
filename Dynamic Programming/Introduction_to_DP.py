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


























