"""
📌 Problem: Set Matrix Zeroes
----------------------------------------
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.
You must do it **in-place** (i.e., without using additional memory for another matrix).

📥 Input:
matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]

📤 Output:
matrix = [[1,0,1],
          [0,0,0],
          [1,0,1]]

✅ Constraint:
- The matrix must be modified in-place.
- No new matrix or deep copy is allowed.

----------------------------------------
🧠 Solution Strategy:
We use two sets:
- `zero_rows` → to track all row indices that need to be zeroed
- `zero_cols` → to track all column indices that need to be zeroed

Steps:
1. First Pass:
   - Traverse the matrix and record the rows and columns where a 0 is found.
2. Second Pass:
   - For all recorded rows, set the entire row to 0.
3. Third Pass:
   - For all recorded columns, set the entire column to 0.

This ensures that we only modify the matrix after identifying which parts need to change.

----------------------------------------
🧪 Example:

Input:
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

Output:
    matrix = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]

----------------------------------------
⏱ Time and Space Complexity:

- Time Complexity: O(m * n)
    - One pass to find all 0s, another two passes to set rows and columns
- Space Complexity: O(m + n)
    - For storing indices of rows and columns containing 0
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Modifies the input matrix in-place such that if an element is 0,
        its entire row and column are set to 0.

        :param matrix: List of Lists of integers (m x n matrix)
        :return: None (modifies matrix in-place)
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # Step 1: Identify all rows and columns that need to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Step 2: Zero out the identified rows
        for i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

        # Step 3: Zero out the identified columns
        for j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0


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

    # Apply the in-place modification
    Solution().setZeroes(matrix)

    print("\nModified Matrix:")
    for row in matrix:
        print(row)
