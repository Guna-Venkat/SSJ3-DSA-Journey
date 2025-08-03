"""
📌 Problem: Best Time to Buy and Sell Stock (Leetcode 121)
----------------------------------------------------------
You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.

You want to maximize your profit by choosing a **single day to buy one stock** and choosing a
**different day in the future to sell that stock**.

Return the **maximum profit** you can achieve from this transaction.
If no profit is possible, return 0.

📥 Input Examples:
Example 1:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price = 1), sell on day 5 (price = 6), profit = 6 - 1 = 5

Example 2:
    Input: prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: No transaction is done, so profit = 0

🛑 Constraint:
- You must buy before you sell
- Only one transaction allowed

----------------------------------------------------------
🧠 Solution Strategy: One-Pass Greedy Approach

We maintain:
- `min_price` → the lowest price seen so far (ideal buy day)
- `max_profit` → the highest profit we can achieve by selling on current day after buying at `min_price`

🚦 Algorithm Steps:
1. Initialize:
    - `min_price = ∞` (to track the lowest price)
    - `max_profit = 0`

2. For each price in prices:
    - If current price < `min_price`: update `min_price`
    - Else: calculate profit = price - `min_price`
        - If profit > `max_profit`: update `max_profit`

3. Return `max_profit` at the end.

----------------------------------------------------------
🔄 Step-by-step Trace:

Input: prices = [7, 1, 5, 3, 6, 4]

- Day 0: price = 7 → min_price = 7
- Day 1: price = 1 → min_price = 1
- Day 2: price = 5 → profit = 4 → max_profit = 4
- Day 3: price = 3 → profit = 2 → max_profit remains 4
- Day 4: price = 6 → profit = 5 → max_profit = 5
- Day 5: price = 4 → profit = 3 → max_profit remains 5

Final Output: 5

----------------------------------------------------------
⏱ Time and Space Complexity:
- Time Complexity: O(n) → Single pass through the array
- Space Complexity: O(1) → Constant space, in-place calculations

----------------------------------------------------------
📝 Additional Notes:
- This is a classic greedy problem.
- Can be used in real-time financial analysis (e.g., max profit calculation with a single trade).
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit possible with one buy and one sell.

        :param prices: List[int] - List of stock prices by day
        :return: int - Maximum achievable profit
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit


# 🔧 Test Case
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    print("Stock Prices by Day:")
    print(prices)

    result = Solution().maxProfit(prices)

    print("\nMaximum Profit:", result)
