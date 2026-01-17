Medium/best-time-to-buy-and-sell-stock-ii.py

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
    
        # Start from the second day (index 1)
        for i in range(1, len(prices)):
            # If the price today is higher than yesterday, 
            # we pretend we bought yesterday and sold today.
            if prices[i] > prices[i-1]:
                # Add the difference to our profit
                total_profit += (prices[i] - prices[i-1])
                
        return total_profit
