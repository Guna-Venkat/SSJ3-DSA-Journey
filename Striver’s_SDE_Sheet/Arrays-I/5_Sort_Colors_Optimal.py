"""
📌 Problem: Sort Colors (Leetcode 75)
-------------------------------------
Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We use the integers:
- 0 → red
- 1 → white
- 2 → blue

📥 Input Examples:
Example 1:
    Input: nums = [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

Example 2:
    Input: nums = [2, 0, 1]
    Output: [0, 1, 2]

🛑 Constraint:
- You must solve this in-place.
- You cannot use the sort() library function or extra arrays.
-------------------------------------
🧠 Solution Strategy: Dutch National Flag Algorithm

We maintain three pointers:
- `low`: everything left of this is 0 (red zone)
- `mid`: current pointer we're evaluating
- `high`: everything right of this is 2 (blue zone)

Regions:
| Index Range       | Contents          |
|-------------------|-------------------|
| 0 to low - 1      | All 0s (reds)     |
| low to mid - 1    | All 1s (whites)   |
| mid to high       | Unknown elements  |
| high + 1 to end   | All 2s (blues)    |

🚦 Algorithm Steps:
1. Initialize `low = 0`, `mid = 0`, `high = len(nums) - 1`
2. While `mid <= high`:
    - If nums[mid] == 0:
        → Swap with nums[low], increment both `low` and `mid`
    - If nums[mid] == 1:
        → It's already in correct place, just increment `mid`
    - If nums[mid] == 2:
        → Swap with nums[high], decrement `high`
        → Don't increment `mid` (the swapped-in value could be 0, 1, or 2)

-------------------------------------
🔄 Visual Example:

Input: [2, 0, 2, 1, 1, 0]

Step-by-step trace:
Start: low = 0, mid = 0, high = 5

→ nums[mid] = 2 → swap with nums[5] → [0, 0, 2, 1, 1, 2]
→ nums[mid] = 0 → swap with nums[0] → [0, 0, 2, 1, 1, 2]
→ nums[mid] = 0 → swap with nums[1] → [0, 0, 2, 1, 1, 2]
→ nums[mid] = 2 → swap with nums[4] → [0, 0, 1, 1, 2, 2]
→ nums[mid] = 1 → move mid++
→ nums[mid] = 1 → move mid++
→ done!

Final: [0, 0, 1, 1, 2, 2]

-------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n) → Single pass through array
- Space Complexity: O(1) → In-place, constant extra space

-------------------------------------
✅ Where Else Can This Be Used?
This pattern is useful for:

🔹 3-way partitioning problems:
Grouping elements into < pivot, == pivot, > pivot (used in QuickSort 3-way)

Problems with exactly 3 categories to sort/group (often seen in interview problems)

🔹 Similar problems:
Leetcode 75 – Sort Colors

Sort 0s, 1s, 2s in binary array

Partitioning intervals or ratings like ["low", "medium", "high"]
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the colors in-place using the Dutch National Flag algorithm.

        :param nums: List[int] - List containing only 0s, 1s, and 2s
        :return: None (modifies nums in-place)
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# 🔧 Test Case
if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]

    print("Original array:")
    print(nums)

    Solution().sortColors(nums)

    print("\nSorted array:")
    print(nums)
