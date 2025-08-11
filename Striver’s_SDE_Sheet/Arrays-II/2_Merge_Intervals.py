"""
📌 Problem: Merge Intervals (Leetcode 56)
------------------------------------------
You are given an array of intervals where `intervals[i] = [start_i, end_i]`.
The goal is to merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

📥 Input Examples:
Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Intervals [1,3] and [2,6] overlap, so they are merged into [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] overlap, so they are merged into [1,5].

Example 3:
    Input: intervals = []
    Output: []
    Explanation: No intervals provided, so return an empty list.

----------------------------------------------------------
🧠 Solution Strategy: Sorting + Iterative Merge

To merge intervals efficiently:
1. Sort intervals based on the **start time**.
2. Initialize a `merged` list with the first interval.
3. Iterate through each interval:
    - If the current interval overlaps with the last merged one, update the end time to the **maximum** end time.
    - Otherwise, append the current interval to the merged list.

Overlapping condition:
    current_start <= last_end

----------------------------------------------------------
🔄 Step-by-step Trace:

Input: [[1,3],[2,6],[8,10],[15,18]]

Sorted by start:
    [[1,3],[2,6],[8,10],[15,18]]

1. Start with merged = [[1,3]]
2. Compare [2,6] with last = [1,3]:
    - Overlap → merge into [1,6]
3. Compare [8,10] with last = [1,6]:
    - No overlap → append → merged = [[1,6],[8,10]]
4. Compare [15,18] with last = [8,10]:
    - No overlap → append → merged = [[1,6],[8,10],[15,18]]

Final result: [[1,6],[8,10],[15,18]]

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n log n) → Sorting dominates the runtime
- Space Complexity: O(n) → Output list of merged intervals

----------------------------------------------------------
📝 Additional Notes:
- Sorting is necessary because without it, merging would require O(n²) checks
- This is a classic **interval manipulation** problem used in scheduling, booking systems, and range queries
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals into a list of non-overlapping intervals.

        :param intervals: List[List[int]] - List of [start, end] intervals
        :return: List[List[int]] - List of merged non-overlapping intervals
        """
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            # If there is overlap, merge intervals
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged


# 🔧 Test Case
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    print("Original intervals:")
    print(intervals)

    result = Solution().merge(intervals)

    print("\nMerged intervals:")
    print(result)
