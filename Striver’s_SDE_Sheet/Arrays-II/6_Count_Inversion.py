"""
Problem:
--------
Given an integer array nums, return the number of inversions in the array.

Two elements nums[i] and nums[j] form an inversion if:
    nums[i] > nums[j] and i < j.

- A sorted array has an inversion count of 0.
- An array sorted in descending order has the maximum inversion count.

Examples:
---------
Example 1:
Input: nums = [2, 3, 7, 1, 3, 5]
Output: 5

Explanation:
Inversions are:
(2, 1) -> indexes (0, 3)
(3, 1) -> indexes (1, 3)
(7, 1) -> indexes (2, 3)
(7, 3) -> indexes (2, 4)
(7, 5) -> indexes (2, 5)

Example 2:
Input: nums = [-10, -5, 6, 11, 15, 17]
Output: 0
Explanation: Array is already sorted, so no inversions.

Solution Strategy:
------------------
We use a modified merge sort to count inversions efficiently.
1. Divide the array into halves recursively.
2. Count inversions in the left half and right half.
3. Count inversions while merging:
   - If arr[i] > arr[j] and i < j, then all elements from arr[i] to arr[mid] will be greater than arr[j],
     so we can count them in bulk as (mid - i + 1).

Time Complexity:
----------------
O(n log n) — due to merge sort.

Space Complexity:
-----------------
O(n) — temporary array used during merging.

Why merge sort works here:
--------------------------
Merge sort naturally compares elements while merging,
so it can count how many elements are "out of order" without needing nested loops.
"""

from typing import List

class Solution:
    def numberOfInversions(self, nums: List[int]) -> int:
        """
        Counts the number of inversions in the array using a modified merge sort.
        """
        def merge_sort(arr, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            inv_count = merge_sort(arr, left, mid)
            inv_count += merge_sort(arr, mid + 1, right)
            inv_count += merge(arr, left, mid, right)
            return inv_count

        def merge(arr, left, mid, right):
            temp = []
            i, j = left, mid + 1
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    inv_count += (mid - i + 1)  # Count all remaining elements in left half
                    j += 1

            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1

            # Copy sorted elements back into original array
            for k in range(len(temp)):
                arr[left + k] = temp[k]

            return inv_count

        return merge_sort(nums, 0, len(nums) - 1)


# Example usage:
if __name__ == "__main__":
    nums = [2, 3, 7, 1, 3, 5]
    print(Solution().numberOfInversions(nums))  # Expected output: 5
