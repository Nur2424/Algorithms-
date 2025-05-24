def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers):
            return True

    return False


"""
    ° Here’s a simple recursive version of canSum(targetSum, numbers) without using dynamic programming or memoization:

⏱ Time Complexity:

O(n^t)

Where:
	•	t = targetSum
	•	n = number of elements in the numbers array    

🧠 Why?

Each recursive call branches into up to n calls, and the maximum depth of the recursion can be up to targetSum (when we subtract the smallest number, 1, each time).

This results in a tree of recursive calls with:
	•	Branching factor ≈ n
	•	Height ≈ targetSum

Hence:
\text{Total recursive calls} = O(n^t)


🧠 Space Complexity:

O(t)

Because:
	•	At most targetSum calls will be on the call stack at any one time (linear depth).

⸻

⚠️ Example:

Calling canSum(50, [1, 2, 5]) without memoization will be incredibly slow, as it explores an exponential number of paths.

"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False

"""

🔍 How It Works:
	•	We try subtracting each number in the list from targetSum.
	•	If any recursive call returns True, that means it’s possible to reach the sum.
	•	Memoization is used to avoid recomputing the same subproblem.
	•	Base case:
	•	If targetSum == 0, return True.
	•	If targetSum < 0, return False.

💡 Example Walkthrough

Let’s take canSum(7, [2, 3]):
	•	Try 2:
→ canSum(5, [2, 3])
→ Try 2: canSum(3)
→ Try 2: canSum(1)
→ Try 2: canSum(-1) → False
→ Try 3: canSum(-2) → False
→ Try 3: canSum(0) → ✅ True

This path: 3 + 2 + 2 = 7 → returns True

⸻

🚀 Time & Space Complexity
	•	Time Complexity:
O(targetSum × n)
where n is the length of the array
(Because we only compute each targetSum once, and for each, try n numbers)
	•	Space Complexity:
O(targetSum) — for the recursion stack and memo dictionary

 """

