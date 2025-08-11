"""
📌 Problem: Merge Sorted Array (Leetcode 88)
---------------------------------------------
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single sorted array in-place.

⚠ Important:
- nums1 has a length of m + n
- The first m elements are the meaningful data
- The last n elements are placeholders (0s) and should be replaced during merging
- nums2 has exactly n elements

📥 Input Examples:
Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3
           nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

Example 2:
    Input: nums1 = [1], m = 1
           nums2 = [], n = 0
    Output: [1]

Example 3:
    Input: nums1 = [0], m = 0
           nums2 = [1], n = 1
    Output: [1]

----------------------------------------------------------
🧠 Solution Strategy: Two-pointer (From End)

Merging from the back ensures we do not overwrite elements in nums1 that are yet to be placed.
Steps:
1. Initialize three pointers:
    - `p1` → last valid element in nums1 (m - 1)
    - `p2` → last element in nums2 (n - 1)
    - `p`  → last position in nums1 (m + n - 1)
2. While `p1 >= 0` and `p2 >= 0`:
    - Place the larger of nums1[p1] or nums2[p2] at nums1[p]
    - Move the pointer corresponding to the placed element
3. If nums2 still has elements left, copy them to nums1

----------------------------------------------------------
🔄 Step-by-step Trace:

Input:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6], n = 3

Pointers initially:
    p1 = 2, p2 = 2, p = 5

Compare nums1[2] = 3 and nums2[2] = 6 → place 6 at nums1[5]
    nums1 = [1,2,3,0,0,6]
    p2 = 1, p = 4

Compare nums1[2] = 3 and nums2[1] = 5 → place 5 at nums1[4]
    nums1 = [1,2,3,0,5,6]
    p2 = 0, p = 3

Compare nums1[2] = 3 and nums2[0] = 2 → place 3 at nums1[3]
    nums1 = [1,2,3,3,5,6]
    p1 = 1, p = 2

Compare nums1[1] = 2 and nums2[0] = 2 → place 2 at nums1[2]
    nums1 = [1,2,2,3,5,6]
    p2 = -1 → done

Final Output: [1,2,2,3,5,6]

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(m + n) → Single pass through both arrays
- Space Complexity: O(1) → In-place merging

----------------------------------------------------------
📝 Additional Notes:
- This is a common array manipulation problem used in merging logs, sorted datasets, and versioned data.
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in non-decreasing order, in-place.

        :param nums1: List[int] - First sorted array with extra space at the end
        :param m: int - Number of valid elements in nums1
        :param nums2: List[int] - Second sorted array
        :param n: int - Number of elements in nums2
        :return: None (modifies nums1 in-place)
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy remaining elements from nums2 (if any)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# 🔧 Test Case
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m, n = 3, 3

    print("Before merge:")
    print(nums1)

    Solution().merge(nums1, m, nums2, n)

    print("\nAfter merge:")
    print(nums1)
