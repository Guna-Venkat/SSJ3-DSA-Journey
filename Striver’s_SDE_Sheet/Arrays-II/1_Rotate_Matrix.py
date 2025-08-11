"""
Problem:
---------
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees clockwise.

You must rotate the image in-place, meaning you cannot allocate another 2D matrix for the rotation.

Example 1:
----------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
----------
Input: matrix = [[5,1,9,11],
                 [2,4,8,10],
                 [13,3,6,7],
                 [15,14,12,16]]
Output: [[15,13,2,5],
         [14,3,4,1],
         [12,6,8,9],
         [16,7,10,11]]

Solution Strategy:
------------------
We can achieve a 90° clockwise rotation using two main steps:
1. **Transpose the matrix**: Swap elements across the main diagonal (i.e., element at [i][j] swaps with [j][i] for j > i).
2. **Reverse each row**: This simulates the effect of rotating each layer 90° clockwise.

Why this works:
---------------
- Transposing converts rows to columns.
- Reversing each row then reorders columns to achieve the final rotation.

Time Complexity:
----------------
O(n^2) — We visit each cell once during transpose and once during row reversal.

Space Complexity:
-----------------
O(1) — Rotation is done in-place without extra storage.

Example Walkthrough:
--------------------
Input:
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]

Step 1: Transpose
[ [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9] ]

Step 2: Reverse each row
[ [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3] ]   <- Final rotated matrix
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the matrix 90 degrees clockwise in-place.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix (swap elements across the diagonal)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# Example usage:
if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(mat)
    print(mat)  # Expected output: [[7,4,1],[8,5,2],[9,6,3]]
