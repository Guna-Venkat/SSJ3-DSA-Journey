"""
LeetCode Problem 50: Pow(x, n)
------------------------------

Problem Statement:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

------------------------------------------------------------

Solution Strategy:
1. The naive solution multiplies x repeatedly n times, which would take O(n).
2. Instead, we use the concept of **Binary Exponentiation** (a.k.a. Fast Power):
   - If n is even → x^n = (x^2)^(n/2)
   - If n is odd → x^n = x * (x^2)^((n-1)/2)
3. This reduces the time complexity to O(log n).
4. If n is negative, we compute pow(x, -n) and return 1 / result.

------------------------------------------------------------

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1 / (2^2) = 1/4 = 0.25

------------------------------------------------------------

Time Complexity:
- O(log n), since we halve the exponent in each step.

Space Complexity:
- O(1), since only a few variables are used.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        n_abs = abs(n)

        # Binary exponentiation
        while n_abs > 0:
            if n_abs % 2 == 1:  # if n is odd
                res *= x
            x *= x
            n_abs //= 2

        return res if n >= 0 else 1 / res


# -------------------------
# Example Runs (Uncomment to test)
# -------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0, 10))    # 1024.0
    print(sol.myPow(2.1, 3))     # 9.261000000000001
    print(sol.myPow(2.0, -2))    # 0.25
    print(sol.myPow(2.0, 0))     # 1.0
