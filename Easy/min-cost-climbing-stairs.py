Easy/min-cost-climbing-stairs.py

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost = [0]*(n+1)

        # Can start @ index 0 or 1 with no cost
        min_cost[0] = 0
        min_cost[1] = 0

        for i in range(2, n+1):
            min_cost[i] = min(min_cost[i-2] + cost[i-2], min_cost[i-1] + cost[i-1])
        
        return min_cost[-1]
