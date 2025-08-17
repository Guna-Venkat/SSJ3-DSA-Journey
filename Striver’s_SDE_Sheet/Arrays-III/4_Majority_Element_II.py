"""
LeetCode Problem: Majority Element II
-------------------------------------

Problem Statement:
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

------------------------------------------------------------

Solution Strategy:
1. At most two elements can appear more than ⌊n/3⌋ times.
2. Use an extended version of the **Boyer-Moore Voting Algorithm**:
   - First pass: Identify up to two potential candidates.
   - Second pass: Verify their actual counts.
3. Collect and return all elements that appear more than ⌊n/3⌋ times.

------------------------------------------------------------

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

------------------------------------------------------------

Time Complexity:
- O(n), since we iterate through the array twice.

Space Complexity:
- O(1), only a few variables used.
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Step 1: Identify potential candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify the candidates
        result = []
        for c in [candidate1, candidate2]:
            if c is not None and nums.count(c) > len(nums) // 3:
                result.append(c)
        
        return result


# -------------------------
# Example Runs (Uncomment to test)
# -------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))    # [3]
    print(sol.majorityElement([1]))        # [1]
    print(sol.majorityElement([1,2,3,1,2,1,2,1]))  # [1, 2]
