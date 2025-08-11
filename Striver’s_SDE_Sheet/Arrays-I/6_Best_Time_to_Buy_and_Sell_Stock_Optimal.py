"""
📌 Problem: Rotate Image (Leetcode 48)
----------------------------------------------------------
You are given an `n x n` 2D matrix representing an image.
Rotate the image by **90 degrees clockwise**.

You must rotate the image **in-place**, meaning you should modify the input matrix directly without allocating another 2D matrix.

📥 Input Examples:
Example 1:
    Input: matrix = [[1,2,3],
                     [4,5,6],
                     [7,8,9]]
    Output: [[7,4,1],
             [8,5,2],
             [9,6,3]]

Example 2:
    Input: matrix = [[5,1,9,11],
                     [2,4,8,10],
                     [13,3,6,7],
                     [15,14,12,16]]
    Output: [[15,13,2,5],
             [14,3,4,1],
             [12,6,8,9],
             [16,7,10,11]]

🛑 Constraints:
- matrix.length == n
- matrix[i].length == n
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

----------------------------------------------------------
🧠 Solution Strategy: Transpose + Reverse Rows

We can achieve the 90° rotation in two main steps:

1. **Transpose the matrix** → Swap elements across the diagonal.
   - After this step, rows become columns.

2. **Reverse each row** → This gives the final rotated matrix.

🚦 Algorithm Steps:
1. Let `n` = number of rows/columns.
2. For each `i` in `[0, n)` and `j` in `[i+1, n)`:
   - Swap `matrix[i][j]` and `matrix[j][i]`.
3. For each row in the matrix:
   - Reverse it in-place.

----------------------------------------------------------
🔄 Step-by-step Trace:

Input:
    [[1,2,3],
     [4,5,6],
     [7,8,9]]

Step 1: Transpose (swap across diagonal)
    [[1,4,7],
     [2,5,8],
     [3,6,9]]

Step 2: Reverse each row
    [[7,4,1],
     [8,5,2],
     [9,6,3]]

Final Output:
    [[7,4,1],
     [8,5,2],
     [9,6,3]]

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n²) → Every element is visited once during transpose and once during row reversal.
- Space Complexity: O(1) → In-place rotation without extra data structures.

----------------------------------------------------------
📝 Additional Notes:
- Works for any n x n square matrix.
- The transpose step is a common trick in image processing tasks.
"""

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the given n x n matrix 90 degrees clockwise in-place.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# 🔧 Test Case
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    Solution().rotate(matrix)

    print("\nRotated Matrix:")
    for row in matrix:
        print(row)
