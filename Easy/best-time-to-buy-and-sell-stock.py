Easy/best-time-to-buy-and-sell-stock.py

# Notes:
# Keep track of 2 things:
# - Lowest price we've seen so far (potential buy price)
# - Max profit we can make if we sold at current price.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            # Potential profit if sold today
            curr_profit = prices[i] - min_price
            
            # Update max_profit if curr_profit is better
            if curr_profit > max_profit:
                max_profit = curr_profit
            
            # Update the min_price
            if prices[i] < min_price:
                min_price = prices[i]
                
        return max_profit
