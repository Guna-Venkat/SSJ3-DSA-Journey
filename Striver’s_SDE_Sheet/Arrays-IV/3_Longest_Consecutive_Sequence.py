"""
📌 Problem: Longest Consecutive Sequence (Leetcode 128)
-------------------------------------------------------
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

📥 Input Examples:
Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Example 3:
    Input: nums = [1,0,1,2]
    Output: 3

----------------------------------------------------------
🧠 Solution Strategy: Hash Set for Fast Lookups

To find the longest consecutive sequence efficiently:
1. Add all numbers to a set for O(1) lookups.
2. For each number, check if it's the start of a sequence (i.e., x-1 not in set).
3. If so, count the length of the sequence by incrementing and checking membership.
4. Track the maximum length found.

----------------------------------------------------------
🔄 Step-by-step Trace:

Input: nums = [100,4,200,1,3,2]
Set: {1, 2, 3, 4, 100, 200}
- Start at 1 (since 0 not in set), sequence: 1,2,3,4 → length 4
- Other numbers either not start of a sequence or shorter

Final result: 4

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n) → Each number processed at most twice
- Space Complexity: O(n) → Set stores all unique numbers

----------------------------------------------------------
📝 Additional Notes:
- This technique is useful for problems involving consecutive elements or ranges.
- Avoids sorting (O(n log n)), meeting the O(n) requirement.
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)          # O(n) build
        best = 0

        for x in s:            # each x considered once
            if x - 1 not in s: # start of a run?
                y = x
                while y in s:  # walk the run
                    y += 1
                best = max(best, y - x)

        return best

# 🔧 Test Case
if __name__ == "__main__":
    nums1 = [100,4,200,1,3,2]
    print("Input nums:", nums1)
    print("Longest consecutive sequence length:", Solution().longestConsecutive(nums1))

    nums2 = [0,3,7,2,5,8,4,6,0,1]
    print("\nInput nums:", nums2)
    print("Longest consecutive sequence length:", Solution().longestConsecutive(nums2))

    nums3 = [1,0,1,2]
    print("\nInput nums:", nums3)
    print("Longest consecutive sequence length:", Solution().longestConsecutive(nums3))