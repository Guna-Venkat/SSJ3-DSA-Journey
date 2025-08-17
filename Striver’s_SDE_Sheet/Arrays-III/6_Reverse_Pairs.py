"""
LeetCode Problem: Reverse Pairs
-------------------------------

Problem Statement:
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:
- 0 <= i < j < nums.length
- nums[i] > 2 * nums[j]

------------------------------------------------------------

Solution Strategy:
1. Use a modified merge sort to count reverse pairs efficiently.
2. During the merge step, for each element in the left half, count how many elements in the right half satisfy nums[i] > 2 * nums[j].
3. Merge the two halves to maintain sorted order, which allows efficient counting in future steps.

Step-by-Step Algorithm:
- Recursively split the array into halves using merge sort.
- For each left element, use a pointer to scan the right half and count valid reverse pairs.
- Merge the two halves back together in sorted order.
- Accumulate the count from each merge step and return the total.

------------------------------------------------------------

Example 1:
Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:
Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

------------------------------------------------------------

Time Complexity:
- O(n log n), due to the merge sort and counting during merge.

Space Complexity:
- O(n), for the temporary array used during merging.

Additional Notes:
- This technique (modified merge sort) is useful for counting pairs with specific conditions in sorted subarrays.
- The approach leverages the sorted property to efficiently count pairs, avoiding brute-force O(n^2) solutions.
"""

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l: int, r: int) -> int:
            if l >= r:
                return 0

            mid = (l + r) // 2
            count = merge_sort(l, mid) + merge_sort(mid + 1, r)

            # Count cross-pairs: for each i in left half, find how many j in right half
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))

            # Merge the two sorted halves
            temp = []
            p1, p2 = l, mid + 1
            while p1 <= mid and p2 <= r:
                if nums[p1] <= nums[p2]:
                    temp.append(nums[p1])
                    p1 += 1
                else:
                    temp.append(nums[p2])
                    p2 += 1
            while p1 <= mid:
                temp.append(nums[p1])
                p1 += 1
            while p2 <= r:
                temp.append(nums[p2])
                p2 += 1

            nums[l:r+1] = temp
            return count

        return merge_sort(0, len(nums) - 1)


# -------------------------
# Example Runs (Uncomment to test)
# -------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.reversePairs([1,3,2,3,1]))    # 2
    print(sol.reversePairs([2,4,3,5,1]))    # 3
    print(sol.reversePairs([5,4,3,2,1]))    #