"""
📌 Problem: Four Sum (Leetcode 18)
-----------------------------------
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

📥 Input Examples:
Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
    Explanation:
        - After sorting: [2,2,2,2,2]
        - The only quadruplet that sums to 8 is [2,2,2,2].
        - The algorithm skips duplicates for all indices, so only one unique quadruplet is returned.

----------------------------------------------------------
🧠 Solution Strategy: Sorting + Two Pointers

To find all unique quadruplets:
1. Sort the array to simplify duplicate handling and enable two-pointer technique.
2. Use two nested loops to fix the first two numbers (`i` and `j`).
3. For each pair, use two pointers (`left` and `right`) to find pairs that sum to the required value.
4. Skip duplicates for all indices to ensure unique quadruplets.

----------------------------------------------------------
🔄 Step-by-step Trace:

Input: nums = [1,0,-1,0,-2,2], target = 0

Sorted: [-2,-1,0,0,1,2]
1. Fix i=-2, j=-1, left=0, right=2
2. Check sum, move pointers, skip duplicates
3. Collect quadruplets that sum to target

Input: nums = [2,2,2,2,2], target = 8

Sorted: [2,2,2,2,2]
1. Fix i=0 (2), j=1 (2), left=2, right=4
2. Sum: 2+2+2+2=8 → add [2,2,2,2]
3. Move pointers and skip duplicates, no other unique quadruplet possible.

Final results:
    [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] for first example
    [[2,2,2,2]] for second example

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n³) → Three nested loops and two pointers
- Space Complexity: O(k) → Output list of quadruplets

----------------------------------------------------------
📝 Additional Notes:
- This technique generalizes to kSum problems.
- Sorting and careful duplicate handling are key for unique results.
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res

# 🔧 Test Case
if __name__ == "__main__":
    nums1 = [1,0,-1,0,-2,2]
    target1 = 0
    print("Input nums:", nums1)
    print("Target:", target1)
    result1 = Solution().fourSum(nums1, target1)
    print("Unique quadruplets that sum up to the target:", result1)

    nums2 = [2,2,2,2,2]
    target2 = 8
    print("\nInput nums:", nums2)
    print("Target:", target2)
    result2 = Solution().fourSum(nums2, target2)
    print("Unique quadruplets that sum up to the target:", result2)