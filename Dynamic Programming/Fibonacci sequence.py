# Brute Force Approach: To find the nth Fibonacci number using a brute force approach, you would simply add the (n-1)th and (n-2)th Fibonacci numbers.

# Python program to find 
# fibonacci number using recursion.

# Function to find nth fibonacci number
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# ---------------------------------------------------------------------------------------------------

"""

Using Memoization Approach - O(n) Time and O(n) Space

To achieve this in our example we simply take an memo array initialized to -1. 
As we make a recursive call, we first check if the value stored in the memo array corresponding to that position is -1. 
The value -1 indicates that we haven't calculated it yet and have to recursively compute it. 
The output must be stored in the memo array so that, next time, if the same value is encountered, it can be directly used from the memo array.   

"""

# Python program to find
# fibonacci number using memoization.
def fibRec(n, memo):
  
    # Base case
    if n <= 1:
        return n

    # To check if output already exists
    if memo[n] != -1:
        return memo[n]

    # Calculate and save output for future use
    memo[n] = fibRec(n - 1, memo) + \
              fibRec(n - 2, memo)
    return memo[n]

def fib(n):
    memo = [-1] * (n + 1)
    return fibRec(n, memo)

n = 5
print(fib(n)) # 5

# ---------------------------------------------------------------------------------------------------

"""

Using Tabulation Approach - O(n) Time and O(n) Space

In this approach, we use an array of size (n + 1), often called dp[], to store Fibonacci numbers. 
The array is initialized with base values at the appropriate indices, such as dp[0] = 0 and dp[1] = 1. 
Then, we iteratively calculate Fibonacci values from dp[2] to dp[n] by using the relation dp[i] = dp[i-1] + dp[i-2]. 
This allows us to efficiently compute Fibonacci numbers in a loop. 
Finally, the value at dp[n] gives the Fibonacci number for the input n, as each index holds the answer for its corresponding Fibonacci number.

"""
# Python program to find
# fibonacci number using tabulation.
def fibo(n):
    dp = [0] * (n + 1)

    # Storing the independent values in dp
    dp[0] = 0
    dp[1] = 1

    # Using the bottom-up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

n = 5
print(fibo(n)) # 5

# ---------------------------------------------------------------------------------------------------

"""

Using Space Optimised Approach - O(n) Time and O(1) Space

In the above code, we can see that the current state of any fibonacci number depends only on the previous two values. 
So we do not need to store the whole table of size n+1 but instead of that we can only store the previous two values. 

"""

# Python program to find
# fibonacci number using space optimised.
def fibo(n):
    prevPrev, prev, curr = 0, 1, 1

    # Using the bottom-up approach
    for i in range(2, n + 1):
        curr = prev + prevPrev
        prevPrev = prev
        prev = curr

    return curr

n = 5
print(fibo(n)) # 5




