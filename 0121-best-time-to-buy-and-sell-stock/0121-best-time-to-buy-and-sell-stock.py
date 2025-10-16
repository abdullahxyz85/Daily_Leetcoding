class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Step 1: Start with no profit and set the first price as the minimum
        min_price = prices[0]
        max_profit = 0

        # Step 2: Loop through each price in the list
        for price in prices:
            # If the current price is less than the min_price, update min_price
            if price < min_price:
                min_price = price
            else:
                # Otherwise, calculate profit for selling today
                profit = price - min_price
                # If this profit is greater than max_profit, update it
                if profit > max_profit:
                    max_profit = profit

        # Step 3: Return the highest profit found
        return max_profit
