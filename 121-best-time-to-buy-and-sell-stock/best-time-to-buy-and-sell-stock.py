class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize with a very large number
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)  # Update the lowest price
            profit = price - min_price  # Calculate potential profit
            max_profit = max(max_profit, profit)  # Update max profit if needed

        return max_profit



        