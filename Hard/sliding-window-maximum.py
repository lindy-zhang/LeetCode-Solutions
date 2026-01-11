Hard/sliding-window-maximum.py

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Output array:
        output = []
        left, right = 0, 0 
        q = collections.deque() # Contains indices rather than values
        while right < len(nums):
            # While smaller values exist in our queue
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            # Remove left val from window
            if left > q[0]:
                q.popleft(
            if right + 1 >= k:
                output.append(nums[q[0]])
                left += 1
            right+=1
        return output
