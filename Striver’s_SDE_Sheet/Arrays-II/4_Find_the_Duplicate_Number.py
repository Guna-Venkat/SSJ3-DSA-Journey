"""
📌 Problem: Find the Duplicate Number (Leetcode 287)
----------------------------------------------------
Given an array nums containing n + 1 integers, where each integer is in the range [1, n] inclusive:
- There is exactly one repeated number.
- The duplicate may appear more than once.

Constraints:
- You must not modify the input array (read-only).
- You must solve the problem using only constant extra space.
- The runtime complexity must be less than O(n²).

📥 Input Examples:
Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Example 3:
    Input: nums = [3,3,3,3,3]
    Output: 3

----------------------------------------------------------
🧠 Solution Strategy: Floyd's Tortoise and Hare (Cycle Detection)
Why it works:
- The problem can be modeled as finding the start of a cycle in a linked list.
- Treat each array value as a pointer to the next index.
- Since there is one duplicate, this forms a cycle.

Steps:
1. Phase 1: Detect cycle.
   - Use two pointers: `slow` (moves 1 step), `fast` (moves 2 steps).
   - Keep moving until they meet.

2. Phase 2: Find cycle start (duplicate number).
   - Reset `slow` to nums[0].
   - Move both pointers 1 step at a time until they meet again.
   - The meeting point is the duplicate.

----------------------------------------------------------
🔄 Step-by-step Trace:
Example: nums = [1,3,4,2,2]

Phase 1:
    slow = nums[0] = 1
    fast = nums[nums[0]] = nums[1] = 3
    Move until slow == fast:
        slow → 3
        fast → nums[nums[3]] = nums[2] = 4
        ...
        Eventually slow and fast meet at value 2

Phase 2:
    Reset slow = nums[0] = 1
    Move both 1 step at a time:
        slow = 3, fast = 3 → meeting point = 2 (duplicate)

Output: 2

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n) → At most 2 passes through the array
- Space Complexity: O(1) → Only uses a constant number of variables

----------------------------------------------------------
📝 Additional Notes:
- This is an elegant cycle detection algorithm (Floyd’s Tortoise and Hare).
- Works without modifying the array or using extra data structures.
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in the given array using Floyd's cycle detection algorithm.

        :param nums: List[int] - Array containing n+1 integers, with one duplicate.
        :return: int - The duplicate number.
        """
        # Phase 1: Detect the intersection point
        slow = nums[0]
        fast = nums[nums[0]]  # Fast pointer starts 2 steps ahead
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# 🔧 Test Case
if __name__ == "__main__":
    nums = [1,3,4,2,2]
    print("Duplicate number:", Solution().findDuplicate(nums))  # Expected: 2
