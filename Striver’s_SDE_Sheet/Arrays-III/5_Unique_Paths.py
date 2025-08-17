"""
LeetCode Problem: Unique Paths
------------------------------

Problem Statement:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

------------------------------------------------------------

Solution Strategy:
1. Use dynamic programming to count the number of ways to reach each cell.
2. Since the robot can only move right or down, the number of ways to reach cell (i, j) is the sum of ways to reach (i-1, j) and (i, j-1).
3. Optimize space by using a single 1D array to store the number of ways for each column.

------------------------------------------------------------

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

------------------------------------------------------------

Time Complexity:
- O(m * n), since we iterate through the grid.

Space Complexity:
- O(n), using a single array for columns.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]


# -------------------------
# Example Runs (Uncomment to test)
# -------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 7))    # 28
    print(sol.uniquePaths(3, 2))    # 3
    print(sol.uniquePaths(7, 3))    # 28
    print(sol.uniquePaths(3, 3))    #