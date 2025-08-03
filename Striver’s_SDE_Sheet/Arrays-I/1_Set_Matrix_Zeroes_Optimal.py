"""
📌 Problem: Set Matrix Zeroes (In-Place Optimized)
-------------------------------------------------
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.
You must do it **in-place**, without using extra space for another matrix.

📥 Input Example:
matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

📤 Output:
matrix = [
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0]
]

-------------------------------------------------
🧠 Optimized Solution Strategy:

To reduce space complexity to O(1), we use the **first row and first column** of the matrix itself
as flags/markers to indicate which rows or columns need to be set to zero.

Steps:
1. Check if the first row and first column themselves need to be zeroed by scanning them separately.
2. Traverse the matrix (excluding first row and column). If a cell is 0, set:
    - matrix[i][0] = 0 (mark this row)
    - matrix[0][j] = 0 (mark this column)
3. Traverse the matrix again (excluding first row and column), and for each cell:
    - If matrix[i][0] == 0 or matrix[0][j] == 0 → set cell to 0.
4. Finally, zero out the first row and/or first column if they were marked in step 1.

-------------------------------------------------
⏱ Time and Space Complexity:

- Time Complexity: O(m * n) – Every cell is visited at most twice.
- Space Complexity: O(1) – No extra space used (in-place modification).
"""

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modifies the input matrix in-place. If an element is 0,
        its entire row and column are set to 0 using an optimized space approach.

        :param matrix: List of Lists of integers (m x n matrix)
        :return: None
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Step 1: Determine if first row or column should be zero
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Step 2: Use first row and column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero out first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 5: Zero out first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


# 🔧 Test Case
if __name__ == "__main__":
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    Solution().setZeroes(matrix)

    print("\nModified Matrix:")
    for row in matrix:
        print(row)
