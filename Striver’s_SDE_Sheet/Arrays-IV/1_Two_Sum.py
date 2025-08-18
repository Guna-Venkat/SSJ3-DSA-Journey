"""
📌 Problem: Two Sum (Leetcode 1)
---------------------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

📥 Input Examples:
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

----------------------------------------------------------
🧠 Solution Strategy: Hash Map Lookup

To find two numbers that sum to the target efficiently:
1. Iterate through the array, keeping track of each number's index in a hash map.
2. For each number, compute its complement (target - num).
3. If the complement exists in the hash map, return the indices.
4. Otherwise, store the current number and its index in the hash map.

This avoids checking every pair (O(n^2)) and solves the problem in linear time.

----------------------------------------------------------
🔄 Step-by-step Trace:

Input: nums = [2,7,11,15], target = 9

1. i=0, num=2, complement=7
   - 7 not in hash_map → store 2:0
2. i=1, num=7, complement=2
   - 2 is in hash_map → return [0,1]

Final result: [0,1]

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n) → Each element is processed once
- Space Complexity: O(n) → Hash map stores up to n elements

----------------------------------------------------------
📝 Additional Notes:
- This technique is useful for pair-sum problems and can be adapted for 3Sum, 4Sum, etc.
- Hash maps provide constant-time lookups, making this approach efficient.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # Stores {num: index}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i

# 🔧 Test Case
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print("Input nums:", nums)
    print("Target:", target)
    result = Solution().twoSum(nums, target)
    print("Indices of numbers adding to target:", result)  # Output: [0, 1]