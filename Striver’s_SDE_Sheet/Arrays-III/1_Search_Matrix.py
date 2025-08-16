"""
LeetCode Problem 74: Search a 2D Matrix
--------------------------------------

Problem Statement:
You are given an m x n integer matrix with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return True if target is in matrix or False otherwise.

You must write a solution in O(log(m * n)) time complexity.

------------------------------------------------------------

Solution Strategy:
1. Since each row is sorted and the first element of a row is greater than the last 
   element of the previous row, we can treat the 2D matrix like a flattened sorted array.
2. However, instead of actually flattening, we do two levels of binary search:
   - First binary search: Find the potential row where the target can lie.
   - Second binary search: Search within that row.
3. If target is found → return True, else → return False.

------------------------------------------------------------

Example 1:
Input: matrix = [[1,3,5,7],
                 [10,11,16,20],
                 [23,30,34,60]], target = 3
Output: True

Example 2:
Input: matrix = [[1,3,5,7],
                 [10,11,16,20],
                 [23,30,34,60]], target = 13
Output: False

------------------------------------------------------------

Time Complexity:
- Binary search on rows → O(log m)
- Binary search on chosen row → O(log n)
Total = O(log m + log n) ≈ O(log(m * n))

Space Complexity:
- O(1), no extra space used apart from variables.
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Step 1: Binary search on rows to find the possible row
        low, high = 0, m - 1
        row = -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        if row == -1:
            return False  # target can't be in any row

        # Step 2: Binary search in the chosen row
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False


# -------------------------
# Example Runs (Uncomment to test)
# -------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False
