"""
LeetCode Problem 169: Majority Element
--------------------------------------

Problem
-------
Given an integer array `nums` of size `n`, return the **majority element** —
the element that appears **more than ⌊n/2⌋ times**.
You may assume the majority element **always exists**.

Examples
--------
1) Input: nums = [3, 2, 3]
   Output: 3

2) Input: nums = [2, 2, 1, 1, 1, 2, 2]
   Output: 2

Step-by-Step Solution (Boyer–Moore Voting)
------------------------------------------
Idea: Pair off different elements; only the majority survives the cancellations.

1) Initialize:
   - `count = 0`
   - `candidate = None`

2) For each `num` in `nums`:
   - If `count == 0`, set `candidate = num` (start/refresh a candidate).
   - If `num == candidate`, increment `count` by 1.
   - Else, decrement `count` by 1.

3) After one pass, return `candidate`.
   - Since a majority (> n/2) exists, the final `candidate` must be it.

Quick Dry Run
-------------
nums = [2, 2, 1, 1, 1, 2, 2]
- Start: count=0 -> candidate=2, count=1
- See 2: matches -> count=2
- See 1: different -> count=1
- See 1: different -> count=0
- count==0 -> candidate=1, count=1
- See 2: different -> count=0
- count==0 -> candidate=2, count=1
Return 2

Additional Notes
----------------
- Algorithm Used: **Boyer–Moore Majority Vote**.
- Correctness Intuition:
  - Every time you see a non-candidate element, you "cancel" one candidate vote.
  - Since the majority element appears > n/2 times, it can’t be fully canceled.
- Time Complexity: **O(n)** (single pass).
- Space Complexity: **O(1)**.
- Edge Cases:
  - Any values (positive/negative/zero) are fine.
  - Arrays of length 1 return the only element.
  - Majority is guaranteed by the problem (no need for a second verification pass).
- Alternative (for learning): Use a hashmap/counter to count frequencies, then pick the max — **O(n)** time, **O(n)** space.

Similar Problems
----------------
- LeetCode 229: Majority Element II (elements appearing > ⌊n/3⌋ times).
- Generalized Boyer–Moore for k-majority (appearing > ⌊n/k⌋ times).
- Verify majority when not guaranteed: run Boyer–Moore, then confirm with a second count.

Code
----
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer–Moore Majority Vote Algorithm.
        Returns the element that appears more than floor(n/2) times.
        Assumption: Such an element always exists.
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


# Example usage / simple tests
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))                # Expected: 3
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))    # Expected: 2
