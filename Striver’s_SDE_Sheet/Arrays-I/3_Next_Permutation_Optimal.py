"""
📌 Problem: Next Permutation (Leetcode 31)
------------------------------------------
A **permutation** of an array of integers is an arrangement of its members into a sequence.

You are given an array `nums`, and you must transform it into the **next lexicographically greater permutation**.
If no such arrangement is possible (i.e., it's the last permutation), rearrange it to the **lowest possible order** (i.e., sorted in ascending order).

🔁 You must perform the transformation **in-place** using only constant extra memory.

📥 Input Examples:
Example 1:
    Input: nums = [1, 2, 3]
    Output: [1, 3, 2]

Example 2:
    Input: nums = [3, 2, 1]
    Output: [1, 2, 3]

Example 3:
    Input: nums = [1, 1, 5]
    Output: [1, 5, 1]

----------------------------------------------------------
🧠 Solution Strategy: Reverse Traversal + Swap + Reverse

The key idea is to find the **first number from the end** that breaks the descending order,
then **swap it** with the smallest number greater than it to the right, and finally **reverse**
the rest to get the next lexicographically smallest sequence.

🚦 Algorithm Steps:

1. Traverse from right and find the first decreasing element:
    - i = n - 2
    - while nums[i] >= nums[i + 1]: i -= 1

2. If such an element is found (i ≥ 0):
    - Find the smallest number just **larger than nums[i]** to the right
    - Swap nums[i] and nums[j]

3. Reverse the subarray from i+1 to end to make it smallest lexicographic suffix.

----------------------------------------------------------
🔄 Step-by-step Trace:

Input: nums = [1, 2, 3]
- Step 1: Find i = 1 (because 2 < 3)
- Step 2: Find j = 2 (smallest number > 2 from the right)
- Step 3: Swap → [1, 3, 2]
- Step 4: Reverse suffix (nothing to reverse as it's just [2])

Final: [1, 3, 2]

Input: nums = [3, 2, 1]
- Entire array is in descending order → no i found
- Reverse whole array → [1, 2, 3]

----------------------------------------------------------
⏱ Time and Space Complexity:

- Time Complexity: O(n)
    - Each of the steps (scan, swap, reverse) takes linear time
- Space Complexity: O(1)
    - In-place rearrangement using constant memory

----------------------------------------------------------
📝 Additional Notes:
- This problem is critical for understanding permutation generation
- Can be used in combinatorics, lexicographic ordering, and puzzle problems
"""

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges the numbers into the next lexicographically greater permutation.
        If not possible, rearranges into the lowest possible order (ascending).
        
        :param nums: List[int] - The input permutation
        :return: None (modifies nums in-place)
        """
        n = len(nums)
        i = n - 2

        # Step 1: Find first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            # Step 2: Find next greater element to swap
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the part after i
        nums[i+1:] = nums[i + 1:][::-1]


# 🔧 Test Case
if __name__ == "__main__":
    nums = [1, 2, 3]

    print("Original permutation:")
    print(nums)

    Solution().nextPermutation(nums)

    print("\nNext permutation:")
    print(nums)
