"""

The tribonacci series is a generalization of the Fibonacci sequence where each term is the sum of the three preceding terms.

a(n) = a(n-1) + a(n-2) + a(n-3)
with
a(0) = a(1) = 0, a(2) = 1.

First few numbers in the Tribonacci Sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, ....

Given a value n, task is to print first n Tribonacci Numbers. 

Examples:  

  Input : 5
  Output : 0, 0, 1, 1, 2

  Input : 10
  Output : 0, 0, 1, 1, 2, 4, 7, 13, 24, 44

  Input : 20
  Output : 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136,  5768, 10609, 19513

"""

#-----------------------------------------------------------------------------------------------------------------------

# A simple solution is to simply follow recursive formula and write recursive code for it 

# A simple recursive CPP program to print
# first n Tribonacci numbers.

def printTribRec(n) :
    if (n == 0 or n == 1 or n == 2) :
        return 0
    elif (n == 3) :
        return 1
    else :
        return (printTribRec(n - 1) + 
                printTribRec(n - 2) +
                printTribRec(n - 3))
        

def printTrib(n) :
    for i in range(1, n) :
        print( printTribRec(i) , " ", end = "")
        

# Driver code
n = 10
printTrib(n) # 0 0 1 1 2 4 7 13 24 

# Time complexity of above solution is exponential.


#-----------------------------------------------------------------------------------------------------------------------

# 1) Top-Down Dp Memoization:

def tribonacci(n): 
    h={} #creating the dictionary to store the results
    def tribo(n):
        if n in h:
            return h[n]
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            res=tribo(n-3)+tribo(n-2)+tribo(n-1)
            h[n]=res #storing the results so that we can reuse it again 
        return res
    return tribo(n)
n=10
for i in range(n):
    print(tribonacci(i),end=' ') # 0 0 1 1 2 4 7 13 24 

# Time complexity of above is linear, but it requires extra space.

#-----------------------------------------------------------------------------------------------------------------------

# 2) Bottom-Up DP Tabulation:

# A DP based
# Python 3 
# program to print
# first n Tribonacci
# numbers.

def printTrib(n) :

    dp = [0] * n
    dp[0] = dp[1] = 0;
    dp[2] = 1;

    for i in range(3,n) :
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];

    for i in range(0,n) :
        print(dp[i] , " ", end="")
        

# Driver code
n = 10
printTrib(n) # 0 0 1 1 2 4 7 13 24 

# Time complexity of above is linear, but it requires extra space.

#-----------------------------------------------------------------------------------------------------------------------

# Time complexity of above is linear, but it requires extra space.
  We can optimizes space used in above solution using three variables to keep track of previous three numbers.

# A space optimized
# based Python 3 
# program to print
# first n Tribinocci 
# numbers.

def printTrib(n) :
    if (n < 1) :
        return
 
    # Initialize first
    # three numbers
    first = 0
    second = 0
    third = 1

    print( first , " ", end="")
    if (n > 1) :
        print(second, " ",end="")
    if (n > 2) :
        print(second, " ", end="")

    # Loop to add previous
    # three numbers for
    # each number starting
    # from 3 and then assign
    # first, second, third
    # to second, third, and curr
    # to third respectively
    for i in range(3, n) :
        curr = first + second + third
        first = second
        second = third
        third = curr

        print(curr , " ", end="")
    
    
# Driver code
n = 10
printTrib(n)  # 0 0 0 1 2 4 7 13 24 44 










