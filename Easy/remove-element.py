Easy/remove-element.py

# Notes:
# - Array manipulation
# - Two pointers

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use two pointers
        L = 0
        R = len(nums) - 1
        while L <= R:
            if nums[L] == val:
                # Swap
                nums[L], nums[R] = nums[R], nums[L]
                R -= 1 # Decrement R, but NOT L in case the swapped element is equal to val
            else:
                L += 1
        return L
