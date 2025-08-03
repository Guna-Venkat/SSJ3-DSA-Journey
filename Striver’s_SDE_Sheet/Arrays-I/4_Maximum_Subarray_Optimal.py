"""
📌 Problem: Maximum Subarray (Kadane’s Algorithm)
-------------------------------------------------
Given an integer array `nums`, find the contiguous subarray (containing at least one number)
which has the largest sum, and return its sum.

This is a classic **Dynamic Programming** problem often solved using **Kadane’s Algorithm**.

📥 Input Examples:
Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum = 1.

Example 3:
    Input: nums = [5, 4, -1, 7, 8]
    Output: 23
    Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum = 23.

-------------------------------------------------
🧠 Solution Strategy (Kadane's Algorithm):

- Initialize two variables:
    - `currentSum` → the current running sum (reset to 0 if it goes negative)
    - `maxSum` → the global maximum sum found so far

- Traverse the array:
    - Add each element to `currentSum`
    - If `currentSum` is greater than `maxSum`, update `maxSum`
    - If `currentSum` becomes negative, reset it to 0

This ensures that we always track the best subarray sum efficiently in a single pass.

-------------------------------------------------
⏱ Time and Space Complexity:

- Time Complexity: O(n)
    - We scan the list exactly once
- Space Complexity: O(1)
    - No extra space is used (just two variables)

"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the subarray with the largest sum using Kadane's Algorithm.

        :param nums: List[int] - the input array
        :return: int - the maximum sum of any contiguous subarray
        """
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum += num
            if currentSum > maxSum:
                maxSum = currentSum
            if currentSum < 0:
                currentSum = 0

        return maxSum


# 🔧 Test Case
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print("Input array:")
    print(nums)

    result = Solution().maxSubArray(nums)

    print("\nMaximum subarray sum:", result)
