Medium/jump-game-i.py

# Notes:
# - original mistake: tried to be greedy and always jump max distance possible
# - instead keep track of farthest index possible

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_reach = tracks furthest index we can reach
        max_reach = 0
        
        # Iterate through every index in arr
        for i in range(len(nums)):
            # If currently at an index we cannot reach, return False
            if i > max_reach:
                return False
            
            # Update the furthest index we can reach from here
            # (current position + max jump possible from here)
            max_reach = max(max_reach, i + nums[i])
            
            # If can already reach the end, stop early
            if max_reach >= len(nums) - 1:
                return True
        
        # Check again at the end      
        return max_reach >= len(nums) - 1
